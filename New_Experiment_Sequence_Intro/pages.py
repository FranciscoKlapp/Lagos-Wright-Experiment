
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Welcome(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        return dict(other_participants=self.session.num_participants-1)

    #timeout_seconds =180


class Instructions1_both(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    #timeout_seconds = 240


class Instructions2_both(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    #timeout_seconds = 240
    def vars_for_template(self):
        initial_supply = self.session.num_participants*Constants.token_endowment
        gamma = self.session.config['gamma']
        return dict(initial_supply = initial_supply,
                    gamma = gamma,
                    interest_rate=round((1 - self.session.config['gamma']) * 100, 2),
                    example1 =round((1 - self.session.config['gamma']) * 100, 2)/10*0.8,
                    example2 = round((1 - self.session.config['gamma']) * 100, 2)/10,)


class Instructions3_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        return dict(pairs = round(self.session.num_participants/2 ))
#----------------------------------------------------------------------------------------------------------------------------

class Instructions_DM0_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        return dict(pairs = round(self.session.num_participants/2, 1),
                    treatment = self.session.config['treatment'])

class Instructions_DM1_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        return dict(pairs = round(self.session.num_participants/2, 1))

class Instructions_DM2_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_DM3_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['instructions_DM']

    def vars_for_template(self):
        return dict(uq0 = round((Constants.mu*0**Constants.eta)/Constants.eta,2) ,
                    uq1 = round((Constants.mu*1**Constants.eta)/Constants.eta,2) ,
                    uq2 = round((Constants.mu*2**Constants.eta)/Constants.eta,2) ,
                    uq3 = round((Constants.mu*3**Constants.eta)/Constants.eta ,2),
                    uq4 = round((Constants.mu*4**Constants.eta)/Constants.eta ,2),
                    uq5 = round((Constants.mu*5**Constants.eta)/Constants.eta ,2),
                    uq6 = round((Constants.mu*6**Constants.eta)/Constants.eta ,2),
                    uq7 = round((Constants.mu*7**Constants.eta)/Constants.eta ,2),
                    uq8 = round((Constants.mu*8**Constants.eta)/Constants.eta ,2),
                    uq9 = round((Constants.mu*9**Constants.eta)/Constants.eta ,2),
                    uq10 =round((Constants.mu*10**Constants.eta)/Constants.eta ,2),
                    uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta,2),
                    uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta,2),
                    uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta,2),
                    uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta,2),
                    uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta,2),
                    uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta, 2),
                    uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta, 2),
                    uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta, 2),
                    uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta, 2),
                    uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta, 2),
                    net_uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta-0,2),
                    net_uq1=round((Constants.mu * 1 ** Constants.eta) / Constants.eta-1,2),
                    net_uq2=round((Constants.mu * 2 ** Constants.eta) / Constants.eta-2,2),
                    net_uq3=round((Constants.mu * 3 ** Constants.eta) / Constants.eta-3,2),
                    net_uq4=round((Constants.mu * 4 ** Constants.eta) / Constants.eta-4,2),
                    net_uq5=round((Constants.mu * 5 ** Constants.eta) / Constants.eta-5,2),
                    net_uq6=round((Constants.mu * 6 ** Constants.eta) / Constants.eta-6,2),
                    net_uq7=round((Constants.mu * 7 ** Constants.eta) / Constants.eta-7,2),
                    net_uq8=round((Constants.mu * 8 ** Constants.eta) / Constants.eta-8,2),
                    net_uq9=round((Constants.mu * 9 ** Constants.eta) / Constants.eta-9,2),
                    net_uq10=round((Constants.mu * 10 ** Constants.eta) / Constants.eta-10,2),
                    net_uq11=round((Constants.mu * 11 ** Constants.eta) / Constants.eta-11,2),
                    net_uq12=round((Constants.mu * 12 ** Constants.eta) / Constants.eta-12,2),
                    net_uq13=round((Constants.mu * 13 ** Constants.eta) / Constants.eta-13,2),
                    net_uq14=round((Constants.mu * 14 ** Constants.eta) / Constants.eta-14,2),
                    net_uq15=round((Constants.mu * 15 ** Constants.eta) / Constants.eta-15,2),
                    net_uq16=round((Constants.mu * 16 ** Constants.eta) / Constants.eta-16, 2),
                    net_uq17=round((Constants.mu * 17 ** Constants.eta) / Constants.eta-17, 2),
                    net_uq18=round((Constants.mu * 18 ** Constants.eta) / Constants.eta-18, 2),
                    net_uq19=round((Constants.mu * 19 ** Constants.eta) / Constants.eta-19, 2),
                    net_uq20=round((Constants.mu * 20 ** Constants.eta) / Constants.eta-20, 2)
                    )

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

class Quiz_Intro_DM(Page):
    #timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz_Offer(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.session.config['treatment'] == 'endogen'

    def before_next_page(self):
        if self.timeout_happened:
            self.player.quiz_output_DM = 0
            self.player.quiz_tokens_DM = 0


    form_model = 'player'
    form_fields = ['quiz_output_DM', 'quiz_tokens_DM']

    def vars_for_template(self):
        return dict(uq0=round((Constants.mu * 0 ** Constants.eta) / Constants.eta, 2),
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



class Quiz_Offer_treatment(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM', 'quiz_tokens_DM']
  #  timeout_seconds = 240
    def before_next_page(self):
        if self.timeout_happened:
            self.player.quiz_output_DM = 0
            self.player.quiz_tokens_DM = 0


    def is_displayed(self):
        return self.session.config['treatment'] == 'exogen'

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


class Quiz_Results0(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM_retry', 'quiz_tokens_DM_retry']

    #timeout_seconds = 180

    def is_displayed(self):
        return  self.session.config['treatment'] == 'endogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )


class Quiz_Results0_treatment(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM_retry', 'quiz_tokens_DM_retry']

    #timeout_seconds = 180

    def is_displayed(self):
        return self.session.config['treatment'] == 'exogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )





class Quiz_Results0_b(Page):
    form_model = 'player'


    #timeout_seconds = 180

    def is_displayed(self):
        return  self.player.quiz_tokens_DM_retry != 99 and self.player.quiz_output_DM_retry != 99 and self.session.config['treatment'] == 'endogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )



class Quiz_Results0_b_treatment(Page):
    form_model = 'player'


    #timeout_seconds = 180

    def is_displayed(self):
        return  self.player.quiz_tokens_DM_retry != 99 and self.player.quiz_output_DM_retry != 99 and self.session.config['treatment'] == 'exogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )




class Quiz_Offer2(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.session.config['treatment'] == 'endogen'

    form_model = 'player'
    form_fields = ['quiz_output_DM2', 'quiz_tokens_DM2']


    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )






class Quiz_Offer2_treatment(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM2', 'quiz_tokens_DM2']
  #  timeout_seconds = 240
    def before_next_page(self):
        if self.timeout_happened:
            self.player.quiz_output_DM2 = 0
            self.player.quiz_tokens_DM2 = 0


    def is_displayed(self):
        return self.session.config['treatment'] == 'exogen'

    def vars_for_template(self):
        payoff_aux0=self.participant.payoff+Constants.point_endowment


        return dict(payoff_aux0 =payoff_aux0,
                    player_in_all_rounds_rev=reversed(self.player.in_previous_rounds()),
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






class Quiz_Results1(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM2_retry', 'quiz_tokens_DM2_retry']
    #timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.session.config['treatment'] == 'endogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

class Quiz_Results1_treatment(Page):
    form_model = 'player'
    form_fields = ['quiz_output_DM2_retry', 'quiz_tokens_DM2_retry']
    #timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.session.config['treatment'] == 'exogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )




class Quiz_Results1_b(Page):
    form_model = 'player'


    #timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.player.quiz_tokens_DM2_retry != 99 and self.player.quiz_output_DM2_retry != 99 and self.session.config['treatment'] == 'endogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

class Quiz_Results1_b_treatment(Page):
    form_model = 'player'


    #timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.player.quiz_tokens_DM2_retry != 99 and self.player.quiz_output_DM2_retry != 99 and self.session.config['treatment'] == 'exogen'

    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

#-----------------------------------------------------------------------------------------------------------------------------


class Instructions_CM0_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_CM1_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_CM2_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_CM3_both(Page):
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Quiz_Intro_CM(Page):
    #timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz_ChooseRole_1(Page):
    form_model = 'player'
    form_fields = ['quiz_choose_1']
    #timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Quiz_Results2(Page):
    form_model = 'player'
#    timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1

class Quiz_ChooseRole_2(Page):
    form_model = 'player'
    form_fields = ['quiz_choose_2']
 #   timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1

class Quiz_Results3(Page):
    form_model = 'player'
  #  timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz_CmBuyer(Page):
    form_model = 'player'
    form_fields = ['quiz_cm_bid', 'quiz_prediction1']
   # timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz_Results4(Page):
    form_model = 'player'
#    timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1

class Quiz_CmSeller(Page):
    form_model = 'player'
    form_fields = ['quiz_cm_output_offer', 'quiz_prediction2']

#    timeout_seconds = 240
    def is_displayed(self):
        return self.subsession.round_number == 1



class Quiz_Results5(Page):
    form_model = 'player'
 #   timeout_seconds = 180

    def is_displayed(self):
        return self.subsession.round_number == 1
##----------------------------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------##
class Instructions_final0_both(Page):
 #   timeout_seconds = 180
    def is_displayed(self):
        return self.subsession.round_number == 1
    def js_vars(self):
        return dict(
            mu = Constants.mu,
            eta = Constants.eta
        )

class Instructions_final1_both(Page):
  #  timeout_seconds = 180
    def is_displayed(self):
        return self.subsession.round_number == 1
class Instructions_final2_both(Page):
 #   timeout_seconds = 180
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        payoff_aux0=round(self.player.payoff1+Constants.point_endowment,2)
        return dict(payoff_aux0 =payoff_aux0)
##---------------------------------------------------------------------------------------------------------------------------##
##---------------------------------------------------------------------------------------------------------------------------##


page_sequence = [
                Welcome,   Instructions1_both, Instructions2_both,  Instructions3_both,

                 Instructions_DM0_both, Instructions_DM2_both, Instructions_DM3_both,
                 Quiz_Intro_DM,

                Quiz_Offer, Quiz_Results0, Quiz_Results0_b, Quiz_Offer2, Quiz_Results1,  Quiz_Results1_b,
                Quiz_Offer_treatment, Quiz_Results0_treatment, Quiz_Results0_b_treatment, Quiz_Offer2_treatment, Quiz_Results1_treatment,  Quiz_Results1_b_treatment,


                Instructions_CM0_both,   Instructions_CM2_both, Instructions_CM3_both,
                Quiz_Intro_CM, Quiz_ChooseRole_1, Quiz_Results2, Quiz_ChooseRole_2, Quiz_Results3,

                Quiz_CmBuyer, Quiz_Results4,
                Quiz_CmSeller, Quiz_Results5
                ]