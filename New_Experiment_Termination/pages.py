
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random



class ResultsWaitPage5(WaitPage):
    body_text = 'Waiting for other participants.'
    after_all_players_arrive = 'set_payoff_end'


class Game_Ends(Page):
 #   timeout_seconds = 90

    def vars_for_template(self):
        total2 = self.participant.payoff+self.session.config['participation_fee']
        return dict(total = self.participant.payoff + Constants.point_endowment,
                    seq1 = self.participant.vars['sequence1_payoff'],
                    seq3 = self .participant.vars['sequence3_payoff'],
                    total2=total2,
                    real_money = total2*self.session.config['real_world_currency_per_point'],
                    redemption_code=self.participant.code,
                    label = self.participant.label)

class ExitSurvey(Page):
   #timeout_seconds = 240

   form_model = 'player'

   form_fields = [
       'risk1', 'risk2', 'age', 'field_of_study',
        'GPA',  'math_classes',
        'stats_classes', 'econ_classes', 'CRT1', 'CRT2', 'CRT3', 'CRT4',
   ]


class Payment_Link(Page):
    timeout_seconds = 60
    def vars_for_template(self):
        total2 = self.participant.payoff+self.session.config['participation_fee']
        return dict(total = self.participant.payoff + Constants.point_endowment,
                    seq1 = self.participant.vars['sequence1_payoff'],
                    seq3 = self .participant.vars['sequence3_payoff'],
                    total2=total2,
                    real_money = total2*self.session.config['real_world_currency_per_point'],
                    redemption_code=self.participant.code)




page_sequence = [

                 ResultsWaitPage5, Game_Ends, ExitSurvey, Payment_Link
                ]