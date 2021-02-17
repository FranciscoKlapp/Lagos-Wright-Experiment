
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
doc = ''
class Constants(BaseConstants):
    name_in_url = 'New_Sequence4'
    players_per_group = 2
    num_rounds = 6
    token_endowment =10
    point_endowment=40
    exchange_rate=0.2
  #  gamma=1   # change for Friedman Rule
    q_bar=20
    DM_good = 'Special Good'
    CM_good = 'Regular Good'
    mu = 1.635
    eta = 1-0.224
    max_DM_request = 20
    max_price_prediction= 10

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print(self.get_group_matrix())

    sum_bid = models.FloatField()
    sum_output_offers = models.FloatField()
    price = models.FloatField()
    lump_sum = models.FloatField()
    money_supply = models.FloatField()


    def set_payoff_cm(self):
        self.sum_bid = sum(p.cm_bid for p in self.get_players())
        self.sum_output_offers = sum(p.cm_output_offer for p in self.get_players())

        if self.sum_output_offers > 0 and self.sum_bid > 0:
            self.price = round(self.sum_bid/self.sum_output_offers, 2)

        for p in self.get_players():
            if p.choose == 'Seller':
                if self.sum_output_offers > 0 and self.sum_bid > 0:
                    p.payoff2 = -p.cm_output_offer  # linear function
                    p.tokens_end_end = round(p.tokens_end_lump+self.price * p.cm_output_offer, 2)
                else:
                    p.payoff2 = 0
                    p.tokens_end_end = round(p.tokens_end_lump, 2)

            if p.choose == 'Buyer':
                if self.sum_output_offers > 0 and self.sum_bid > 0:
                    p.payoff2 = round(p.cm_bid/self.price, 2)   #linear function
                    p.tokens_end_end = round(p.tokens_end_lump - p.cm_bid,2)
                else:
                    p.payoff2 = 0
                    p.tokens_end_end = round(p.tokens_end_lump, 2)

class Group(BaseGroup):

    def set_tokens_dm(self):

        buyer = self.get_player_by_role("buyer")
        seller = self.get_player_by_role("seller")

        if self.subsession.round_number == 1:
            buyer.tokens_begin = Constants.token_endowment
            seller.tokens_begin = Constants.token_endowment


        else:
            buyer.tokens_begin = buyer.in_round(self.round_number - 1).tokens_end_end
            seller.tokens_begin = seller.in_round(self.round_number - 1).tokens_end_end


    def set_payoff_dm(self):
        buyer = self.get_player_by_role("buyer")
        seller = self.get_player_by_role("seller")

        if seller.offer_accept == True:
            seller.payoff1 = - buyer.output_request  #linear function
            seller.tokens_end = seller.tokens_begin+buyer.token_offer
            buyer.payoff1 = round((Constants.mu*buyer.output_request**Constants.eta)/Constants.eta, 2) #concave function
            buyer.tokens_end = buyer.tokens_begin - buyer.token_offer
            if buyer.token_offer > 0 and buyer.output_request > 0:
                buyer.implicit_price = round(buyer.token_offer / buyer.output_request,2)
                seller.implicit_price = round(buyer.token_offer / buyer.output_request,2)
            else:
                buyer.implicit_price = 0
                seller.implicit_price = 0
        else:
            seller.payoff1 = 0
            seller.tokens_end = seller.tokens_begin
            buyer.payoff1 = 0
            buyer.tokens_end = buyer.tokens_begin
            buyer.implicit_price = 0
            seller.implicit_price = 0

        self.subsession.money_supply = Constants.token_endowment*self.session.num_participants
        self.subsession.lump_sum = round((1-self.session.config['gamma']) * self.subsession.money_supply / self.session.num_participants,2)
        buyer.interest = round(buyer.tokens_end*(1-self.session.config['gamma']),2)
        seller.interest = round(seller.tokens_end*(1-self.session.config['gamma']),2)

        buyer.tokens_end_lump = round(buyer.tokens_end - self.subsession.lump_sum+buyer.interest, 2)
        seller.tokens_end_lump = round(seller.tokens_end - self.subsession.lump_sum+seller.interest, 2)



    def set_payoff_combine(self):
        for p in self.get_players():
            p.payoff = p.payoff1+p.payoff2


    def set_payoff_final(self):
        for p in self.get_players():
            p.participant.vars['sequence4_payoff']= p.participant.payoff+Constants.point_endowment
            p.participant.payoff = 0




class Player(BasePlayer):

    def other_player(self):
        return self.get_others_in_group()[0]


    output_request = models.FloatField(label='How many units  would you like to buy?', max=Constants.q_bar, min=0)


    implicit_price = models.FloatField()
    offer_accept = models.BooleanField(choices=[[True, 'Accept'], [False, 'Reject']],
                                       label='Do you accept this offer?',
                                       widget=widgets.RadioSelect
                                       )
    tokens_begin = models.FloatField()
    tokens_end = models.FloatField()
    tokens_end_lump = models.FloatField()
    tokens_end_end = models.FloatField()
    money= models.FloatField()
    payoff1 = models.FloatField()
    payoff2 = models.FloatField()
    interest = models.FloatField()

    choose = models.StringField(
            label = '',
            choices=[['Buyer','Consumer (earn Points, spend Tokens)'], ['Seller','Producer (earn Tokens, spend Points)']],
            doc="""This player's decision""",
            widget=widgets.RadioSelect
            )

    prediction1 = models.FloatField()

    token_offer = models.FloatField(label='How many Tokens would you like to offer for those units?')
    def token_offer_max(self):
        return self.tokens_begin

    #cm_output_offer = models.FloatField(label='', max=Constants.q_bar, min=0)
    cm_output_offer = models.FloatField(label='', min=0)
    def cm_output_offer_max(self):
        return self.participant.payoff+Constants.point_endowment+self.payoff1


   #cm_bid = models.FloatField(label='', max=Constants.token_endowment, min=0)
    cm_bid = models.FloatField(label='', min=0, widget=widgets.Slider(attrs={'step': '0.01'}, show_value=True))
    def cm_bid_max(self):
        return self.tokens_end_lump


    def role(self):
        if self.id_in_group == 1:
            return 'buyer'
        if self.id_in_group == 2:
            return 'seller'

