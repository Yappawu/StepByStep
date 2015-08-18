# -*- coding: utf-8 -*-
from stepbystep import db
from datetime import datetime


class RoleModel(db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)

    @staticmethod
    def insert_roles():
        roles = {
                'program_1': '程序设计基础I（SDUTOJ）',
                'program_2': '程序设计基础II（SDUTOJ）',
                'data_structure': '数据结构（SDUTOJ）',
                'junior': '算法初级（POJ）',
                'middle': '算法中级（POJ）',
                'senior': '算法高级（POJ）',
                'statistics': '做题统计',
                'admin': '管理员'
        }
        for r in roles:
            role = RoleModel.objects(name=r).first()
            if role is None:
                role = RoleModel(name=r)
            role.description = roles[r]
            role.save()

    def __unicode__(self):
        return self.name

    meta = {
        'collection': 'Role'
    }
