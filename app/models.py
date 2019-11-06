#!/usr/bin/env python3
# encoding: utf-8
# @File: models.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 13:48
from . import db


class Words(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(64))
    created_at = db.Column(db.String(32))
    updated_at = db.Column(db.String(32))

    def keys(self):
        return ('id', 'content', 'created_at', 'updated_at')

    def __getitem__(self, item):
        return getattr(self, item)


class TrendingPools(db.Model):
    __tablename__ = 'trending_pools'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_date = db.Column(db.String(32))
    created_at = db.Column(db.String(32))
    updated_at = db.Column(db.String(32))
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    word = db.relationship('Words', backref=db.backref('trending_pools', lazy='select'))
    must = db.Column(db.Integer)


class Sannos(db.Model):
    __tablename__ = 'sannos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    anno_name = db.Column(db.String(32), unique=True)
    created_at = db.Column(db.String(32))
    updated_at = db.Column(db.String(32))
    active = db.Column(db.Integer)

    def to_obj(dic):
        sanno = Sannos()
        sanno.anno_name = dic.anno_name
        sanno.created_at = dic.created_at
        sanno.updated_at = dic.updated_at
        sanno.active = dic.active
        return sanno


# 联合主键
class SannosWords(db.Model):
    __tablename__ = 'sannos_words'
    __table_args__ = (db.PrimaryKeyConstraint('sanno_id', 'word_id'),)
    sanno_id = db.Column(db.Integer, db.ForeignKey('sannos.id'))
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    # sannos = relationship('Sannos', foreign_keys=[sanno_id])
    # word = relationship('Words', foreign_keys=[word_id])


"""
lass EssayStateAssociations(db.Model):
    __tablename__ = 'essay_associations'
    __table_args__ = (
        PrimaryKeyConstraint('application_essay_id', 'theme_essay_id'),
    )

    application_essay_id = db.Column(
        db.Integer,
        db.ForeignKey("application_essay.id"))
    theme_essay_id = db.Column(
        db.Integer,
        db.ForeignKey("theme_essay.id"))
    state = db.Column(db.String, default="pending")
"""
