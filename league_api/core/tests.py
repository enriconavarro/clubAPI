from django.test import TestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from .models import Team, League, Player


def get_team(name):
    try:
        return Team.objects.get(name=name)
    except ObjectDoesNotExist:
        return None


def get_league(name):
    try:
        return League.objects.get(name=name)
    except ObjectDoesNotExist:
        return None


def create_team(id=1, name='TestTeam1', city='TestCity1',
                cc=1, coach='TestCoach1'):
    team = Team(id, name, city, cc, coach)
    team.save()

    return team


class TeamTestCase(TestCase):
    name = ''
    city = ''
    cw = 0
    coach = ''

    def setUp(self):
        self.name = 'TestTeam1'
        self.city = 'TestCity1'
        self.cw = 1
        self.coach = 'TestCoach1'

    def create_and_assert_team(self):
        team = Team(name=self.name, city=self.city, championships_won=self.cw,
                    coach=self.coach)
        team.save()

        self.assertEqual(team.name, self.name)
        self.assertEqual(team.city, self.city)
        self.assertEqual(team.championships_won, self.cw)
        self.assertEqual(team.coach, self.coach)

        return team

    def test_team_edit(self):
        team = self.create_and_assert_team()

        self.name = 'TestTeam2'
        team.name = self.name
        self.city = 'TestCity2'
        team.city = self.city
        self.cw = 10
        team.championships_won = self.cw
        self.coach = 'TestCoach2'
        team.coach = self.coach
        team.save()

        self.assertEqual(team.name, self.name)
        self.assertEqual(team.city, self.city)
        self.assertEqual(team.championships_won, self.cw)
        self.assertEqual(team.coach, self.coach)

    def test_team_delete(self):
        team = self.create_and_assert_team()
        team.delete()

        self.assertIsNone(get_team(self.name))


class TeamFunctionalTestCase(TestCase):
    name = ''
    city = ''
    cw = 0
    coach = ''
    client = None

    def setUp(self):
        self.name = 'TestTeam1'
        self.city = 'TestCity1'
        self.cw = 1
        self.coach = 'TestCoach1'
        self.client = Client()

    def create_and_assert_team(self):
        response = self.client.post('/teams/', {
            'name': self.name,
            'city': self.city,
            'championships_won': self.cw,
            'coach': self.coach
        })

        self.assertEqual(response.status_code, 201)

    def test_f_team_get(self):
        self.create_and_assert_team()
        team_id = get_team(self.name).id
        response = self.client.get(f'/teams/{team_id}/')

        self.assertEqual(response.status_code, 200)

    def test_f_team_put(self):
        self.create_and_assert_team()
        team_id = get_team(self.name).id
        self.name = 'TestTeam2'
        self.city = 'TestCity2'
        self.cw = 10
        self.coach = 'TestCoach2'
        response = self.client.put(f'/teams/{team_id}/', {
            'id': team_id,
            'name': self.name,
            'city': self.city,
            'championships_won': self.cw,
            'coach': self.coach
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_f_team_export(self):
        self.create_and_assert_team()
        team_id = get_team(self.name).id
        response = self.client.get(f'/teams/{team_id}/export/')

        self.assertEqual(response.status_code, 200)

    def test_f_team_delete(self):
        self.create_and_assert_team()
        team_id = get_team(self.name).id
        response = self.client.delete(f'/teams/{team_id}/')

        self.assertEqual(response.status_code, 204)


class LeagueTestCase(TestCase):
    name = ''
    country = ''
    cc = None
    teams = []

    def setUp(self):
        self.name = 'TestLeague1'
        self.country = 'TestCountry1'
        team = create_team()
        self.cc = team
        self.teams = [team]

    def create_and_assert_league(self):
        league = League(name=self.name, country=self.country,
                        current_champion=self.cc)
        league.save()
        league.teams.set(self.teams)

        self.assertEqual(league.name, self.name)
        self.assertEqual(league.country, self.country)
        self.assertEqual(league.current_champion.name, self.cc.name)

        return league

    def test_league_edit(self):
        league = self.create_and_assert_league()

        self.league = 'TestLeague2'
        league.name = self.name
        self.country = 'TestCountry2'
        league.country = self.country
        team2 = create_team(2, 'TestTeam2', 'Testcity2', 2, 'TestCoach2')
        league.current_champion = team2
        league.save()
        league.teams.set([team2])

        self.assertEqual(league.name, self.name)
        self.assertEqual(league.country, self.country)
        self.assertEqual(league.current_champion.name, team2.name)

    def test_league_delete(self):
        league = self.create_and_assert_league()
        league.delete()

        self.assertIsNone(get_league(self.name))


class LeagueFunctionalTestCase(TestCase):
    name = ''
    country = ''
    cc = None
    teams = []
    client = None

    def setUp(self):
        self.name = 'TestLeague1'
        self.country = 'TestCountry1'
        team = create_team()
        self.cc = team
        self.teams = [team]
        self.client = Client()

    def create_and_assert_league(self):
        response = self.client.post('/leagues/', {
                'name': self.name,
                'country': self.country,
                'current_champion': self.teams[0].name,
                'teams': [
                    {
                        'id': get_team(self.teams[0].name).id
                    }
                ]
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

    def test_f_league_get(self):
        self.create_and_assert_league()
        league_id = get_league(self.name).id
        response = self.client.get(f'/leagues/{league_id}/')

        self.assertEqual(response.status_code, 200)

    def test_f_league_put(self):
        self.create_and_assert_league()
        league_id = get_league(self.name).id
        self.league = 'TestLeague2'
        self.country = 'TestCountry2'
        team2 = create_team(2, 'TestTeam2', 'Testcity2', 2, 'TestCoach2')
        response = self.client.put(f'/leagues/{league_id}/', {
                'name': self.name,
                'country': self.country,
                'current_champion': team2.name,
                'teams': [
                    {
                        'id': get_team(self.teams[0].name).id
                    },
                    {
                        'id': get_team(team2.name).id
                    }
                ]
            },
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_f_league_export(self):
        self.create_and_assert_league()
        league_id = get_league(self.name).id
        response = self.client.get(f'/leagues/{league_id}/export/')

        self.assertEqual(response.status_code, 200)

    def test_f_league_delete(self):
        self.create_and_assert_league()
        league_id = get_league(self.name).id
        response = self.client.delete(f'/leagues/{league_id}/')

        self.assertEqual(response.status_code, 204)
