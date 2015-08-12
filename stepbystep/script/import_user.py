# -*- coding: utf-8 -*-

import csv
import sys
sys.path.append('../../')


def import_user():
    from stepbystep.models import UserModel, AccountItem, Account
    with open('stepbystep_user.csv', 'r') as users:
        for sid, name, grade, sdut_id, poj_id in csv.reader(
                users.read().splitlines()[1:]):
            if sid and name and grade:
                user = UserModel.objects(
                    username=sid).first()
                if not user:
                    user = UserModel.create_user(
                        username=sid,
                        password='1234567890',
                        name=name,
                        grade=grade
                    )
                if sdut_id:
                    sdut_account = AccountItem.objects.create(
                        origin_oj='sdut',
                        username=sdut_id
                    )
                    user.sdut = Account(
                        user_id=sdut_id,
                        account=sdut_account
                    )
                    account_crawler.delay(
                        origin_oj='sdut',
                        username=sdut_id
                    )
                if poj_id:
                    poj_account = AccountItem.objects.create(
                        origin_oj='poj',
                        username=poj_id
                    )
                    user.poj = Account(
                        user_id=poj_id,
                        account=poj_account
                    )
                    account_crawler.delay(
                        origin_oj='poj',
                        username=poj_id
                    )
                user.save()


if __name__ == '__main__':
    from stepbystep import app
    from stepbystep.libs.tasks import account_crawler
    with app.app_context():
        import_user()
