#! -*- coding: utf-8 -*-

import csv

import sys
sys.path.append('../../')


def import_category_problem(origin_oj):
    from stepbystep.models import ProblemModel, CategoryModel
    p_count = 0
    with open('stepbystep_%s.csv' % origin_oj, 'r') as problems:
        c0 = c1 = c2 = p = None
        c0_count = 0
        for c0, c1, c2, p in csv.reader(problems.read().splitlines()):
            if c0:
                c0 = CategoryModel(
                    name=c0,
                    origin_oj=origin_oj,
                    ordinal=c0_count)
                c0.save()
                c0_count += 1
                c0_temp = c0
            else:
                c0 = c0_temp
            if c1:
                c1 = CategoryModel(name=c1)
                c1.parent = c0
                c1.save()
                c1_temp = c1
            else:
                c1 = c1_temp
            if c2:
                c2 = CategoryModel(name=c2)
                c2.parent = c1
                c2.save()
                c2_temp = c2
            else:
                c2 = c2_temp
            if p:
                p = ProblemModel(
                    origin_oj=origin_oj,
                    problem_id=p,
                    ordinal=p_count)
                p.category = c2
                p.genera = c0
                p.save()
                p_count += 1


if __name__ == '__main__':
    from stepbystep import app
    with app.app_context():
        import_category_problem('poj')
        import_category_problem('sdut')
