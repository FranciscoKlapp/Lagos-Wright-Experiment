
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
doc = ''
class Constants(BaseConstants):
    name_in_url = 'New_SequenceEnds'
    players_per_group = 2
    num_rounds = 1
    token_endowment =10
    point_endowment=40
    exchange_rate=0.25

    q_bar=20
    DM_good = 'Special Good'

    mu = 1.635
    eta = 1-0.224
    max_DM_request = 20
    max_price_prediction= 10

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print(self.get_group_matrix())


class Group(BaseGroup):


    def set_payoff_end(self):
        for p in self.get_players():
            p.participant.payoff = p.participant.vars['sequence1_payoff']+p.participant.vars['sequence3_payoff']



class Player(BasePlayer):

    def other_player(self):
        return self.get_others_in_group()[0]


    risk1 = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        label="1.   In general, how willing are you to take risks?",
        choices=[
        [0, " 0 "],
        [1, " 1 "],
        [2, " 2"],
        [3, " 3"],
        [4, " 4"],
        [5, " 5"],
        [6, " 6"],
        [7, " 7"],
        [8, " 8"],
        [9, " 9"],
        [10, " 10"]
    ]
    )

    risk2 = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        label="2.   How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?",
        choices=[
            [0, " 0 "],
            [1, " 1 "],
            [2, " 2"],
            [3, " 3"],
            [4, " 4"],
            [5, " 5"],
            [6, " 6"],
            [7, " 7"],
            [8, " 8"],
            [9, " 9"],
            [10, " 10"]
        ]
    )



    age = models.IntegerField(
        min=18, max=99,
        label="What is your age?")

    gender = models.IntegerField(
        widget=widgets.RadioSelect,
        label="What is your gender?",
        choices=[
            [1, "Male"],
            [2, "Female"],
            [3, "Other"],
            [4, "Prefer not to say"]
        ]
        )
    ethnicity = models.IntegerField(
        widget=widgets.RadioSelect,
        label="What is your ethnicity?",
        choices=[
            [1, "American Indian or Alaska Native"],
            [2, "Asian"],
            [3, "Black or African American"],
            [4, "Native Hawaiian or Other Pacific Islander"],
            [5, "White"],
            [6, "Other (Please specify below)"],
            [7, "Prefer not to say"]
        ]
    )
    ethnicity_other = models.StringField(
        label="Other ethnicity",
        blank=True
    )

    GPA = models.FloatField(
        widget=widgets.RadioSelect,
        label="What is your GPA?",
        choices=[
            [1, "below 2.00"],
            [2, "2.00-2.25"],
            [3, "2.25 - 2.50"],
            [4, "2.50 - 2.75"],
            [5, "3.00 - 3.25"],
            [6, "3.25 - 3.50"],
            [7, "3.50 - 3.75"],
            [8, "3.75 - 4.00"]
        ]
    )



    field_of_study = models.IntegerField(
        choices=[
            [1, "Arts"],
            [2, "Biological Science"],
            [3, "Business"],
            [4, "Education"],
            [5, "Engineering"],
            [6, "Humanities"],
            [7, "Information & Computer Sciences"],
            [8, "Interdisciplinary Studies"],
            [9, "Nursing Sciences"],
            [10, "Pharmaceutical Sciences"],
            [11, "Physical Sciences"],
            [12, "Public Health"],
            [13, "Social Ecology"],
            [14, "Social Sciences"],
            [15, "Undeclared"],
        ],
        label="Field of Study"
    )
    marital_status = models.IntegerField(
        widget=widgets.RadioSelect,
        label="What is your marital status?",
        choices=[
            [1, "Not married"],
            [2, "Married"],
            [3, "Divorced"],
            [4, "Separated"],
            [5, "Widowed"],
        ]
    )
    college_classification = models.IntegerField(
        widget=widgets.RadioSelect,
        label="What is your classification in college?",
        choices=[
            [1, "Freshman/first-year"],
            [2, "Sophomore"],
            [3, "Junior"],
            [4, "Senior"],
            [5, "Graduate student"],
            [6, "Unclassified"]
        ]
    )
    math_classes = models.IntegerField(
        label="How many math classes have you taken in college?", min=0, max=99,
    )

    stats_classes = models.IntegerField(
        label="How many statistics classes have you taken in college?", min=0, max=99,
    )

    econ_classes = models.IntegerField(
        label="How many economics classes have you taken in college?", min=0, max=99,
    )

    CRT1 = models.IntegerField(
        label="1.   If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how many days would it take them to drink one barrel of water together?", min=0, max=99
    )

    CRT2 = models.IntegerField(
        label="2.   Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class? ", min=0, max=99
    )

    CRT3 = models.IntegerField(
        label="3.   A man buys a pig for $60, sells it for $70, buys it back for $80, and sells it finally for $90. How much ($) has he made?  ", min=0, max=99
    )

    CRT4 = models.IntegerField(
        label="4.   Simon decided to invest $8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. At this point, Simon has:  ",
        widget=widgets.RadioSelect,
        choices=[
            [1, "broke even in the stock market"],
            [2, "is ahead of where he began"],
            [3, "has lost money "]
    ]
    )