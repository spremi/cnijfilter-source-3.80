/*  Canon Inkjet Printer Driver for Linux
 *  Copyright CANON INC. 2001-2012
 *  All Rights Reserved.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307, USA.
 *
 * NOTE:
 *  - As a special exception, this program is permissible to link with the
 *    libraries released as the binary modules.
 *  - If you write modifications of your own for these programs, it is your
 *    choice whether to permit this exception to apply to your modifications.
 *    If you do not wish that, delete this exception.
 */


/*
 * ip2500func.c 
 *
 * A processing function group peculiar to a model.
 */


/*
 * include necessary headers ...
 */
#include "bscc2sts.h"
#include "commonfunc.h"

static int ip2500_setalert(bscc2sts_tbl *p_tbl, int color_num);
static int ip2500_searchcolor(char *p_bsccsts, bscc2sts_tbl *p_tbl, ST_BSCC2STS *p_chgtbl);
static int ip2500_alertsetprocess(char *p_bsccsts, char *p_storetbl, ST_BSCC2STS *p_chgtbl);

ST_BSCC2STS ip2500_cir2fill[]={
  {"100", "100"},
  {"070", "070"},
  {"040", "040"},
  {"010", "010"},
  {"000", "000"},
  {"UK",  "UK" },
  {ENDTAG, ENDTAG}
};

/*
 * Ink information is set from warning and an operator call.
 */
int ip2500_setink(ST_STORESET *p_s, ST_BSCC2STS *p_ct, bscc2sts_tbl *p_tbl, ST_BSCCBUF *p_bsccbuf)
{
  int ret;
  int i=0;
  int color_num=0;
  char *p_tok;

  if( (p_s->p_bsccsts == NULL) || (p_tbl->cartridge[0].type =='?')
      || (p_tbl->warning[0]==NOITEM) || (p_tbl->operator_call[0]==NOITEM)
      || (p_bsccbuf+DWS)->p_bsccsts==NULL || (p_bsccbuf+DOC)->p_bsccsts==NULL ){
	return(OK);
  }

  if( (p_tok=strtok(p_s->p_bsccsts, "=") ) == NULL )
	return(OK);
  ret=commonstssetprocess(p_tok, &(p_tbl->ink[i].color), p_ct);
  if(ret == BADITEM ){
	memset(&p_tbl->ink[0], NOITEM, p_s->size);
	return(OK);
  }
  color_num++;

  while( (p_tok=strtok(NULL, ",")) != NULL ){
	ret=commonstssetprocess(p_tok,p_tbl->ink[i].fill, &ip2500_cir2fill[0]);
	if(ret == BADITEM ){
	  memset(&p_tbl->ink[0], NOITEM, p_s->size);
	  return(OK);
	}
	i++;
	if((p_tok=strtok(NULL, "=")) == NULL){
	  break;
	}
	ret=commonstssetprocess(p_tok,&(p_tbl->ink[i].color), p_ct);
	if(ret == BADITEM ){
	  memset(&p_tbl->ink[0], NOITEM, p_s->size);
	  return(OK);
	}
	color_num++;
  }
  ret=ip2500_setalert(p_tbl, color_num);
  return(OK);
}

static int ip2500_setalert(bscc2sts_tbl *p_tbl, int color_num)
{
  int i,ret;

  for(i=0; i<color_num; i++){
	ret=com_warnoperatechk(p_tbl->warning, p_tbl->ink[i].color, sizeof(p_tbl->warning));
	if( ret == OCCUR ){
	  p_tbl->ink[i].alert = INKWAR;
	} else {
	  p_tbl->ink[i].alert = NOALERT;
	}
  }
  return(OK);
}

int ip2500_setinkalert(ST_STORESET *p_s, ST_BSCC2STS *p_ct, bscc2sts_tbl *p_tbl, ST_BSCCBUF *p_bsccbuf)
{
  int color_num=0;
  char *p_tok;
  extern ST_BSCC2STS ip2500_cir2color[];

  if( (p_tok=strtok(p_s->p_bsccsts, ",") ) == NULL )
	return(OK);

  color_num=ip2500_searchcolor(p_tok,p_tbl,ip2500_cir2color);
  if(color_num == BADITEM ){
	return(OK);
  }

  while( (p_tok=strtok(NULL, ",")) != NULL ){
	ip2500_alertsetprocess(p_tok,&p_tbl->ink[color_num].alert, p_ct);

	if((p_tok=strtok(NULL, ",")) == NULL){
	  break;
	}
	if((p_tok=strtok(NULL, ",")) == NULL){
	  break;
	}

    color_num=ip2500_searchcolor(p_tok,p_tbl,ip2500_cir2color);
    if(color_num == BADITEM ){
	  return(OK);
    }
  }

  return(OK);
}

static int ip2500_searchcolor(char *p_bsccsts, bscc2sts_tbl *p_tbl, ST_BSCC2STS *p_chgtbl)
{
  int i, j;

  for(i=0; (p_chgtbl+i)->bscc!=ENDTAG; i++){
	if( strncmp(p_bsccsts, (p_chgtbl+i)->bscc, strlen((p_chgtbl+i)->bscc)) == 0 ){
	  break;
	}
  }
  if( (p_chgtbl+i)->bscc == ENDTAG )
    return(BADITEM);

  for(j=0; j<MAXip2500COLORNUM; j++){
    if( *( (p_chgtbl+i)->sts ) == p_tbl->ink[j].color )
      return j;
  }

  /* When there is no corresponding item. */
  return(BADITEM);
}

static int ip2500_alertsetprocess(char *p_bsccsts, char *p_storetbl, ST_BSCC2STS *p_chgtbl)
{
  int i;

  for(i=0; (p_chgtbl+i)->bscc!=ENDTAG; i++){
	if( strncmp(p_bsccsts, (p_chgtbl+i)->bscc, strlen((p_chgtbl+i)->bscc)) == 0 ){
	  *p_storetbl=*((p_chgtbl+i)->sts);
	  return(OK);
	}
  }
  /* When there is no corresponding item. */
  return(BADITEM);
}

int ip2500_setwarning(ST_STORESET *p_s, ST_BSCC2STS *p_ct, bscc2sts_tbl *p_tbl, ST_BSCCBUF *p_bsccbuf)
{
  int  i, j;

  if( (p_s->p_bsccsts == NULL) ){
	return(OK);
  }
  for(i=0; p_s->p_storetbl[i]!=INIT; i++);
  p_s->p_bsccsts[2] = 0;
  for(j=0; (p_ct+j)->bscc!=ENDTAG; j++){
	if( strncmp(p_s->p_bsccsts, (p_ct+j)->bscc, strlen((p_ct+j)->bscc)) == 0 ){
	  p_s->p_storetbl[i]=*((p_ct+j)->sts);
	  return(OK);
	}
  }

  return(OK);
}

int ip2500_setcartridgetype(ST_STORESET *p_s, ST_BSCC2STS *p_ct, bscc2sts_tbl *p_tbl, ST_BSCCBUF *p_bsccbuf)
{
  int ret;
  int i;
  char *p_tok;
  char *p_temp;

  if( p_s->p_bsccsts == NULL ){
	return(OK);
  }
  p_temp=(char *)malloc( strlen(p_s->p_bsccsts) + 1 );
  if(p_temp == NULL){
    return(ERR_MEMORY);
  }
  memset (p_temp, 0, strlen(p_s->p_bsccsts) + 1);
  strncpy(p_temp, p_s->p_bsccsts, strlen(p_s->p_bsccsts));
  if( (p_tok=strtok(p_temp,",") ) == NULL )
	return(OK);

  for(i=0; (i<MAXCARTRIDGENUM) && (p_tok!=NULL); i++){
    ret=commonstssetprocess(p_tok,&(p_tbl->cartridge[i].type), p_ct);
    if(ret == BADITEM ){
      memset(&(p_tbl->cartridge[i].type), NOITEM, sizeof(p_tbl->cartridge[i].type));
    }
//iP1300 5line delete
    if((p_tbl->cartridge[i].type==SPACE || p_tbl->cartridge[i].type==CTUNKOWN)){
      if( i == 0 )	p_tbl->cartridge[i].type='L';	// Black or Black High Capa
     else			p_tbl->cartridge[i].type='M';	// Color or Color High Capa
	}

    if( (p_tok=strtok(NULL,",") ) == NULL )
	  break;
  }
  free(p_temp);
  return(OK);
}
