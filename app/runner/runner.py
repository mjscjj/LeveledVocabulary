#!/usr/bin/env python3
# encoding: utf-8
# @File: runner.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 11:47
from os import abort
from flask import current_app as app, abort
from app.models import *
from app.utils import *
from app import db

PAGESIZE = 20


def get_wordid_by_content(content):
    word = db.session.query(Words).filter(Words.content == content).one_or_none()
    db.session.commit()
    if word:
        return word.id


def get_annoid_by_anno(anno):
    result = db.session.query(Sannos).filter(Sannos.anno_name == anno).one_or_none()
    db.session.commit()
    if result:
        return result.id


def validate_sannnos_list(annolist):
    if not isinstance(annolist, list):
        return
    annoall = get_siri_annotationslist()
    array = [x for x in annolist if x not in annoall]
    if len(array) > 0:
        return False
    return True


def get_sannolist_by_word(content):
    wordid = get_wordid_by_content(content)
    if not wordid:
        return
    datas = db.session.query(Sannos, SannosWords).filter(SannosWords.word_id == wordid).filter(
        Sannos.id == SannosWords.sanno_id).all()
    res = []
    for item in datas:
        res.append(item[0].anno_name)
    return res


def add_word(content):
    app.logger.info('add word: {}'.format(content))
    word = db.session.query(Words).filter(Words.content == content).one_or_none()
    if word:
        db.session.query(Words).filter(Words.id == word.id).update({Words.updated_at: get_format_time()})
        db.session.commit()
        return
    word = Words()
    word.created_at = get_format_time()
    word.update_date = get_format_time()
    word.content = content
    db.session.add(word)
    db.session.commit()


def add_annolist_by_word_id(id, annoslist):
    if not isinstance(annoslist, list):
        abort(500)
    if not validate_sannnos_list(annoslist):
        return
    data = db.session.query(SannosWords, Sannos).filter(SannosWords.word_id == id) \
        .filter(SannosWords.sanno_id == Sannos.id).all()
    db.session.commit()
    sannos = {}
    for compound in data:
        sannos[compound[1].id] = compound[1].anno_name
    for an in annoslist:
        if an in sannos.values():
            continue
        # 增加sanno_word
        sw = SannosWords()
        sw.sanno_id = get_annoid_by_anno(an)
        sw.word_id = id
        db.session.add(sw)
        db.session.commit()


# add_annolist_by_word_id(319, ['ovs'])


def add_trending_data(content, annolist, must=-1):
    app.logger.info('add trending word: {}, sannotations: {}, must: {}'.format(content, str(annolist), must))
    if not isinstance(annolist, list):
        abort(500)
    if not validate_sannnos_list(annolist):
        return
    datas = db.session.query(TrendingPools, Words).filter(TrendingPools.word_id == Words.id).filter(
        Words.content == content).one_or_none()
    if datas:
        # 关联对象吧取得 trending_pool
        trending_pools = datas[0]
        if must == -1:
            must = 7
        trending_pools.must = must
        db.session.add(trending_pools)
        # add annotations
        word_id = trending_pools.word_id
        add_annolist_by_word_id(word_id, annolist)
        db.session.commit()
        return

    trending_pools = TrendingPools()
    trending_pools.update_date = get_date()
    trending_pools.created_at = get_format_time()
    trending_pools.updated_at = get_format_time()
    if must == -1:
        must = 7
    trending_pools.must = must
    word = Words()
    word.created_at = get_format_time()
    word.updated_at = get_format_time()
    word.content = content
    # 关联对象
    trending_pools.word = word
    db.session.add(trending_pools)
    db.session.commit()

    for an in annolist:
        sw = SannosWords()
        sw.word_id = get_wordid_by_content(content)
        sw.sanno_id = get_annoid_by_anno(an)
        db.session.add(sw)
    db.session.commit()


def query_trending_pool_list_all():
    querys = db.session.query(TrendingPools).order_by(TrendingPools.id.desc()).limit(10000).all()
    db.session.commit()
    result = []
    for qr in querys:
        result.append(qr.__dict__)
    return result


def get_siri_annotationslist():
    res_objs = db.session.query(Sannos).all()
    db.session.commit()
    list = []
    for anno_obj in res_objs:
        list.append(anno_obj.anno_name)
    db.session.commit()
    return list


def show_result(wordcontent):
    compound = db.session.query(TrendingPools, Words).filter(Words.content == wordcontent).filter(
        TrendingPools.word_id == Words.id).one_or_none()
    db.session.commit()
    sws = db.session.query(SannosWords).filter(SannosWords.word_id == get_wordid_by_content(wordcontent)).all()
    res = []
    for sw in sws:
        res.append(str(sw.word_id))
        res.append(str(sw.__dict__))
    for com in compound:
        res.append(str(com.id))
        res.append(str(com.__dict__))
    return res
