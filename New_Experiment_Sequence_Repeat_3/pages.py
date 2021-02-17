
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

##----------------------------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------##
class Instructions_new_sequence3(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number == 1
    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

##---------------------------------------------------------------------------------------------------------------------------##
##---------------------------------------------------------------------------------------------------------------------------##
class Period_Change(Page):
    timeout_seconds = 45
    def is_displayed(self):
        return self.subsession.round_number > 1

    def vars_for_template(self):
        payoff_aux3 = self.participant.payoff + Constants.point_endowment
        initial_supply = self.session.num_participants * Constants.token_endowment
        return dict(initial_supply=initial_supply,
                    supply=round(initial_supply * self.session.config['gamma'] ** (self.subsession.round_number-2), 2),
                    payoff_aux3 = payoff_aux3,
                    dice = random.randint(1, 5))

class Start(WaitPage):
    body_text = 'Waiting for the other participant.'
    after_all_players_arrive = 'set_tokens_dm'

class Offer(Page):
    form_model = 'player'
    form_fields = ['output_request', 'token_offer']
  #  timeout_seconds = 240
    def before_next_page(self):
        if self.timeout_happened:
            if self.player.tokens_begin < 0:
                self.player.output_request = 0
                self.player.token_offer = -88
            else:
                self.player.output_request = 0
                self.player.token_offer = 0

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.session.config['treatment'] == 'endogen'

    def vars_for_template(self):
        payoff_aux0=self.participant.payoff+Constants.point_endowment
        return dict(payoff_aux0 =payoff_aux0,
                    player_in_all_rounds_rev=reversed(self.player.in_previous_rounds()),
                    uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta, 2),
                    uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta, 2),
                    uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta, 2),
                    uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta, 2),
                    uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta, 2),
                    uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta, 2),
                    uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta, 2),
                    uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta, 2),
                    uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta, 2),
                    uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta, 2),
                    uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta, 2),
                    uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta, 2),
                    uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta, 2),
                    uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta, 2),
                    uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta, 2),
                    uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta, 2),
                    uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta, 2),
                    uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta, 2),
                    uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta, 2),
                    uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta, 2),
                    uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta, 2),
                    net_uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta - 0, 2),
                    net_uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta - 1, 2),
                    net_uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta - 2, 2),
                    net_uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta - 3, 2),
                    net_uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta - 4, 2),
                    net_uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta - 5, 2),
                    net_uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta - 6, 2),
                    net_uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta - 7, 2),
                    net_uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta - 8, 2),
                    net_uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta - 9, 2),
                    net_uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta - 10, 2),
                    net_uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta - 11, 2),
                    net_uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta - 12, 2),
                    net_uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta - 13, 2),
                    net_uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta - 14, 2),
                    net_uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta - 15, 2),
                    net_uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta - 16, 2),
                    net_uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta - 17, 2),
                    net_uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta - 18, 2),
                    net_uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta - 19, 2),
                    net_uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta - 20, 2)
                    )



    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )


class Offer_treatment(Page):
    form_model = 'player'
    form_fields = ['output_request', 'token_offer']
  #  timeout_seconds = 240
    def before_next_page(self):
        if self.timeout_happened:
            if self.player.tokens_begin < 0:
                self.player.output_request = 0
                self.player.token_offer = -88
            else:
                self.player.output_request = 0
                self.player.token_offer = 0

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.session.config['treatment'] == 'exogen'

    def vars_for_template(self):
        payoff_aux0 = self.participant.payoff + Constants.point_endowment
        if self.session.config['gamma'] == 1:
            max_DM = self.player.tokens_begin / (10 / 2)
            exo_price = round(10 / 2, 2)
        else:
            max_DM = self.player.tokens_begin / (10 / 9)
            exo_price = round(10 / 9, 2)

        return dict(max_DM=max_DM,
                    exo_price=exo_price,
                    payoff_aux0=payoff_aux0,
                    player_in_all_rounds_rev=reversed(self.player.in_previous_rounds()),
                    uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta, 2),
                    uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta, 2),
                    uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta, 2),
                    uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta, 2),
                    uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta, 2),
                    uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta, 2),
                    uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta, 2),
                    uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta, 2),
                    uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta, 2),
                    uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta, 2),
                    uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta, 2),
                    uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta, 2),
                    uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta, 2),
                    uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta, 2),
                    uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta, 2),
                    uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta, 2),
                    uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta, 2),
                    uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta, 2),
                    uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta, 2),
                    uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta, 2),
                    uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta, 2),
                    net_uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta - 0, 2),
                    net_uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta - 1, 2),
                    net_uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta - 2, 2),
                    net_uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta - 3, 2),
                    net_uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta - 4, 2),
                    net_uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta - 5, 2),
                    net_uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta - 6, 2),
                    net_uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta - 7, 2),
                    net_uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta - 8, 2),
                    net_uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta - 9, 2),
                    net_uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta - 10, 2),
                    net_uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta - 11, 2),
                    net_uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta - 12, 2),
                    net_uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta - 13, 2),
                    net_uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta - 14, 2),
                    net_uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta - 15, 2),
                    net_uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta - 16, 2),
                    net_uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta - 17, 2),
                    net_uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta - 18, 2),
                    net_uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta - 19, 2),
                    net_uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta - 20, 2)
                    )



    def js_vars(self):
        if self.session.config['gamma'] == 1:
            return dict(
                mu = Constants.mu,
                eta = Constants.eta,
                exogenous_price=(10/2)
            )
        else:
            return dict(
                mu = Constants.mu,
                eta = Constants.eta,
                exogenous_price=(10/9)
            )



class WaitForProposer(WaitPage):
    body_text = 'You met with a Consumer (so you will be a Producer), please wait for their offer.'
    def is_displayed(self):
        return self.player.id_in_group == 2


class Accept(Page):
    form_model = 'player'
    form_fields = ['offer_accept']
   # timeout_seconds = 240
    def before_next_page(self):
        if self.timeout_happened:
            self.player.offer_accept = False

    def is_displayed(self):
        return self.player.id_in_group == 2
    def vars_for_template(self):
        payoff_aux0 = self.participant.payoff + Constants.point_endowment

        for p in self.player.get_others_in_group():

            if p.token_offer>0 or p.output_request>0:
                implicit_price = round(p.token_offer / p.output_request,2)
                payoff_aux_accept = round(self.participant.payoff + Constants.point_endowment-p.output_request,2)
                token_aux_accept = round(self.player.tokens_begin+p.token_offer,2)
            else:
                implicit_price=0    ############..................... check template, should say something liek
                payoff_aux_accept = payoff_aux0
                token_aux_accept = self.player.tokens_begin
            return dict(payoff_aux0 = payoff_aux0,
                    implicit_price=implicit_price,
                    payoff_aux_accept = payoff_aux_accept,
                    token_aux_accept = token_aux_accept,
                    uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta, 2),
                    uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta, 2),
                    uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta, 2),
                    uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta, 2),
                    uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta, 2),
                    uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta, 2),
                    uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta, 2),
                    uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta, 2),
                    uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta, 2),
                    uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta, 2),
                    uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta, 2),
                    uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta, 2),
                    uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta, 2),
                    uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta, 2),
                    uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta, 2),
                    uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta, 2),
                    uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta, 2),
                    uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta, 2),
                    uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta, 2),
                    uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta, 2),
                    uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta, 2),
                    net_uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta - 0, 2),
                    net_uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta - 1, 2),
                    net_uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta - 2, 2),
                    net_uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta - 3, 2),
                    net_uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta - 4, 2),
                    net_uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta - 5, 2),
                    net_uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta - 6, 2),
                    net_uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta - 7, 2),
                    net_uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta - 8, 2),
                    net_uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta - 9, 2),
                    net_uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta - 10, 2),
                    net_uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta - 11, 2),
                    net_uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta - 12, 2),
                    net_uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta - 13, 2),
                    net_uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta - 14, 2),
                    net_uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta - 15, 2),
                    net_uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta - 16, 2),
                    net_uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta - 17, 2),
                    net_uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta - 18, 2),
                    net_uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta - 19, 2),
                    net_uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta - 20, 2)
                    )

class ResultsWaitPage(WaitPage):
    body_text = 'Waiting for Producer to consider your offer.'
    after_all_players_arrive = 'set_payoff_dm'

class Results(Page):
    form_model = 'player'
    timeout_seconds = 45

    def vars_for_template(self):
        payoff_aux = self.participant.payoff+self.player.payoff1+Constants.point_endowment
        return dict(payoff_aux= payoff_aux)

class ChooseRole(Page):
    form_model = 'player'
    form_fields = ['choose']
  #  timeout_seconds = 240

    def before_next_page(self):
        if self.timeout_happened:
            self.player.choose = 'Seller'

    def vars_for_template(self):
        payoff_aux = self.participant.payoff + self.player.payoff1 + Constants.point_endowment
        supply = self.subsession.money_supply

        return dict(supply = supply ,
                    payoff_aux = payoff_aux,
                    interest_rate=round((1-self.session.config['gamma'])*100,2),
                    gamma=self.session.config['gamma']
                    )

class CmBuyer(Page):
    form_model = 'player'
    form_fields = ['cm_bid', 'prediction1']
  #  timeout_seconds = 240
    def is_displayed(self):
        return self.player.choose == 'Buyer'
    def before_next_page(self):
        self.player.cm_output_offer = 0
        if self.timeout_happened:
            self.player.cm_bid = 0
            self.player.cm_output_offer = 0
    def vars_for_template(self):
        supply = self.subsession.money_supply
        payoff_aux = self.participant.payoff + self.player.payoff1 + Constants.point_endowment
        return dict(supply = supply,
                    payoff_aux = payoff_aux)

    def js_vars(self):
        price1 = list(p.price for p in self.subsession.in_all_rounds())
        predicted1  = list(p.prediction1 for p in self.player.in_all_rounds())
        return dict(
            predicted = predicted1,
            price = price1
            )


class CmSeller(Page):
    form_model = 'player'
    form_fields = ['cm_output_offer', 'prediction1']
  #  timeout_seconds = 240
    def is_displayed(self):
        return self.player.choose == 'Seller'
    def before_next_page(self):
        self.player.cm_bid = 0
        if self.timeout_happened:
            self.player.cm_output_offer = 0
            self.player.cm_bid = 0
    def vars_for_template(self):
        supply = self.subsession.money_supply
        payoff_aux = self.participant.payoff + self.player.payoff1 + Constants.point_endowment
        return dict(supply = supply,
                    payoff_aux = payoff_aux)

    def js_vars(self):
        price1 = list(p.price for p in self.subsession.in_all_rounds())
        predicted1  = list(p.prediction1 for p in self.player.in_all_rounds())
        return dict(
            predicted = predicted1,
            price = price1
            )

class ResultsWaitPage2(WaitPage):
    body_text = 'Waiting for other participants.'
    wait_for_all_groups = True
    after_all_players_arrive = 'set_payoff_cm'



class Results2(Page):
    form_model = 'player'
    timeout_seconds = 45

    def vars_for_template(self):
        payoff_aux2 = self.participant.payoff + self.player.payoff1 + self.player.payoff2+Constants.point_endowment

        cm_bid = self.player.cm_bid
        cm_output_offer = self.player.cm_output_offer
        price = self.subsession.price


        if self.subsession.sum_bid ==0 or self.subsession.sum_output_offers==0:
            return dict(
                tokens_seller = 0,
                tokens_buyer = 0,
                units = 0,
                payoff_aux2 = payoff_aux2
            )
        else:
            units = self.player.cm_bid / self.subsession.price
            return dict(
                tokens_seller = round(price*cm_output_offer,2),
                tokens_buyer =  round(cm_bid,2),
                units = round(units,2),
                payoff_aux2=payoff_aux2
            )

    def js_vars(self):
        price1 = list(p.price for p in self.subsession.in_all_rounds())
        predicted1  = list(p.prediction1 for p in self.player.in_all_rounds())
        return dict(
            predicted = predicted1,
            price = price1
            )

class ResultsWaitPage3(WaitPage):
    body_text = 'Waiting for other participants.'
    after_all_players_arrive = 'set_payoff_combine'


class Sequence_Ends(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.session.config['sequences'] != '3'
    def vars_for_template(self):
        total = self.participant.payoff + Constants.point_endowment
        return dict(total=total,
                    real_money = total*self.session.config['real_world_currency_per_point'],
                    redemption_code=self.participant.label)



class Sequence_Ends_Final(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.session.config['sequences'] == '3'
    def vars_for_template(self):
        total = self.participant.payoff + Constants.point_endowment
        return dict(total=total,
                    real_money = total*self.session.config['real_world_currency_per_point'],
                    redemption_code=self.participant.label)




class ResultsWaitPage4(WaitPage):
    body_text = 'Waiting for other participants.'
    after_all_players_arrive = 'set_payoff_final'
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

page_sequence = [

                 Instructions_new_sequence3,
                  Start, Period_Change, Offer, Offer_treatment, WaitForProposer, Accept, ResultsWaitPage, Results,

                 ChooseRole, CmBuyer, CmSeller, ResultsWaitPage2, Results2, ResultsWaitPage3,

                 Sequence_Ends, Sequence_Ends_Final, ResultsWaitPage4
                ]