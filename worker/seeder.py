import random

from django_seed import Seed

from .models import Worker


names = ['John', 'Smith', 'Pol', 'Alexander', 'Will', 'Morgan', 'Freeman', 'Karl']


def seeder_setup(seeder = Seed):
    seeder = seeder.seeder()

    seeder.add_entity(Worker, 2, {
        'full_name': random.choice(names),
        'post': 'Директор',
        'chief': None
    })
    seeder.execute()

    directors = Worker.objects.filter(post='Директор')

    for director in directors:
        seeder.add_entity(Worker, 3, {
            'full_name': random.choice(names),
            'post': 'Зам. Директора',
            'chief': director
        })

    seeder.execute()

    ex_directors = Worker.objects.filter(post='Зам. Директора')

    for ex_director in ex_directors:
        seeder.add_entity(Worker, 4, {
            'full_name': random.choice(names),
            'post': 'Начальник',
            'chief': ex_director
        })

    seeder.execute()

    chiefs = Worker.objects.filter(post='Начальник')

    for chief in chiefs:
        seeder.add_entity(Worker, 5, {
            'full_name': random.choice(names),
            'post': 'Старший работник',
            'chief': chief
        })

    seeder.execute()


    older_workers = Worker.objects.filter(post='Старший работник')

    for older_worker in older_workers:
        seeder.add_entity(Worker, 20, {
            'full_name': random.choice(names),
            'post': 'Работник',
            'chief': older_worker
        })

    seeder.execute()



