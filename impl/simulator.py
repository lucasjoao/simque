import bisect
from impl.constant import constant
from impl.exponential import exponential
from impl.triangular import triangular
from impl.normal import normal
from impl.uniform import uniform
from impl.event import event
from impl.server import server


class simulator(object):

    def create(self, form):
        self.limit_queue = form['limit_queue']

        if form['tec1_aleatory'] == '0':
            self.tec1_distribution = constant(form['tec_c1'])
        elif form['tec1_aleatory'] == '1':
            self.tec1_distribution = normal(
                form['tec_n_media1'], form['tec_n_dp1'])
        elif form['tec1_aleatory'] == '2':
            self.tec1_distribution = uniform(
                form['tec_u_min1'], form['tec_u_max1'])
        elif form['tec1_aleatory'] == '3':
            self.tec1_distribution = triangular(
                form['tec_t_min1'], form['tec_t_mod1'], form['tec_t_max1'])
        elif form['tec1_aleatory'] == '4':
            self.tec1_distribution = exponential(form['tec_e1'])

        if form['tec2_aleatory'] == '0':
            self.tec2_distribution = constant(form['tec_c2'])
        elif form['tec2_aleatory'] == '1':
            self.tec2_distribution = normal(
                form['tec_n_media2'], form['tec_n_dp2'])
        elif form['tec2_aleatory'] == '2':
            self.tec2_distribution = uniform(
                form['tec_u_min2'], form['tec_u_max2'])
        elif form['tec2_aleatory'] == '3':
            self.tec2_distribution = triangular(
                form['tec_t_min2'], form['tec_t_mod2'], form['tec_t_max2'])
        elif form['tec2_aleatory'] == '4':
            self.tec2_distribution = exponential(form['tec_e2'])

        if form['ts1_aleatory'] == '0':
            self.ts1_distribution = constant(form['ts_c1'])
        elif form['ts1_aleatory'] == '1':
            self.ts1_distribution = normal(
                form['ts_n_media1'], form['ts_n_dp1'])
        elif form['ts1_aleatory'] == '2':
            self.ts1_distribution = uniform(
                form['ts_u_min1'], form['ts_u_max1'])
        elif form['ts1_aleatory'] == '3':
            self.ts1_distribution = triangular(
                form['ts_t_min1'], form['ts_t_mod1'], form['ts_t_max1'])
        elif form['ts1_aleatory'] == '4':
            self.ts1_distribution = exponential(form['ts_e1'])

        if form['ts2_aleatory'] == '0':
            self.ts2_distribution = constant(form['ts_c2'])
        elif form['ts2_aleatory'] == '1':
            self.ts2_distribution = normal(
                form['ts_n_media2'], form['ts_n_dp2'])
        elif form['ts2_aleatory'] == '2':
            self.ts2_distribution = uniform(
                form['ts_u_min2'], form['ts_u_max2'])
        elif form['ts2_aleatory'] == '3':
            self.ts2_distribution = triangular(
                form['ts_t_min2'], form['ts_t_mod2'], form['ts_t_max2'])
        elif form['ts2_aleatory'] == '4':
            self.ts2_distribution = exponential(form['ts_e2'])

        if form['tef_aleatory'] == '0':
            self.tef_distribution = constant(form['tef_c'])
        elif form['tef_aleatory'] == '1':
            self.tef_distribution = normal(
                form['tef_n_media'], form['tef_n_dp'])
        elif form['tef_aleatory'] == '2':
            self.tef_distribution = uniform(
                form['tef_u_min'], form['tef_u_max'])
        elif form['tef_aleatory'] == '3':
            self.tef_distribution = triangular(
                form['tef_t_min'], form['tef_t_mod'], form['tef_t_max'])
        elif form['tef_aleatory'] == '4':
            self.tef_distribution = exponential(form['tef_e'])

        if form['tf_aleatory'] == '0':
            self.tf_distribution = constant(form['tf_c'])
        elif form['tf_aleatory'] == '1':
            self.tf_distribution = normal(form['tf_n_media'], form['tf_n_dp'])
        elif form['tf_aleatory'] == '2':
            self.tf_distribution = uniform(form['tf_u_min'], form['tf_u_max'])
        elif form['tf_aleatory'] == '3':
            self.tf_distribution = triangular(
                form['tf_t_min'], form['tf_t_mod'], form['tf_t_max'])
        elif form['tf_aleatory'] == '4':
            self.tf_distribution = exponential(form['tf_e'])

    def start(self):
        self.clock = 0
        self.lef = []
        self.server_1 = server(self.ts1_distribution, self.limit_queue)
        self.server_2 = server(self.ts2_distribution, self.limit_queue)
        event_ent_1 = event(1, 0, self.tec1_distribution.generate(), False)
        event_srv_1 = event(1, 0, self.tef_distribution.generate(), True)
        event_ent_2 = event(2, 0, self.tec2_distribution.generate(), False)
        event_srv_2 = event(2, 0, self.tef_distribution.generate(), True)
        bisect.insort(self.lef, event_ent_1)
        bisect.insort(self.lef, event_ent_2)
        bisect.insort(self.lef, event_srv_1)
        bisect.insort(self.lef, event_srv_2)
        # TODO: variaveis de estado, contadores, estatisticas

    def next_time(self):
        current_event = self.lef.pop(0)
        self.clock += current_event.time
        return current_event
        # TODO: determinar o tipo do próximo evento?

    def event(self, current_event):
        if current_event.about_fail:
            self.execute_fail_event(current_event)
        else:
            self.execute_event(current_event)
        # TODO: atualizar coisas do relatório

    def execute_fail_event(self, current_event):
        entity = current_event.entity
        typo = current_event.typo
        final_time = self.tf_distribution.generate() + self.clock

        if entity:
            # entity 1
            if typo:
                # exit event
                self.server_1.with_error = False
            else:
                # entry event
                self.server_1.with_error = True
                left_event = event(1, 1, final_time, True)
                bisect.insort(self.lef, left_event)

                new_event = event(
                    1, 0, final_time + self.tef_distribution.generate(), True)
                bisect.insort(self.lef, new_event)
        else:
            # entity 2
            if typo:
                # exit event
                self.server_2.with_error = False
            else:
                # entry event
                self.server_2.with_error = True
                left_event = event(2, 1, final_time, True)
                bisect.insort(self.lef, left_event)

                new_event = event(
                    2, 0, final_time + self.tef_distribution.generate(), True)
                bisect.insort(self.lef, new_event)

    def execute_event(self, current_event):
        entity = current_event.entity
        typo = current_event.typo

        if entity:
            # entity 1
            if typo:
                # exit event
                if self.server_1.ef > 0:
                    self.server_1.ef -= 1
                    left_event = event(
                        1, 1, self.server_1.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                    self.server_1.free = False
                else:
                    self.server_1.free = True
                # TODO: statistics
            else:
                # entry event
                if self.server_1.with_error \
                        and not self.server_2.with_error \
                        and self.server_2.free:

                    self.server_2.free = False
                    left_event = event(
                        2, 1, self.server_2.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                elif self.server_1.free:
                    self.server_1.free = False
                    left_event = event(
                        1, 1, self.server_1.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                else:
                    self.server_1.ef += 1

                next_time = self.tec1_distribution.generate() + self.clock
                new_event = event(1, 0, next_time, False)
                bisect.insort(self.lef, new_event)
                # TODO: statistics
        else:
            # entity 2
            if typo:
                # exit event
                if self.server_2.ef > 0:
                    self.server_2.ef -= 1
                    left_event = event(
                        2, 1, self.server_2.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                    self.server_2.free = False
                else:
                    self.server_2.free = True
                # TODO: statistics
            else:
                # entry event
                if self.server_2.with_error \
                        and not self.server_1.with_error \
                        and self.server_1.free:

                    self.server_1.free = False
                    left_event = event(
                        1, 1, self.server_1.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                elif self.server_2.free:
                    self.server_2.free = False
                    left_event = event(
                        2, 1, self.server_2.work() + self.clock, False)
                    bisect.insort(self.lef, left_event)
                else:
                    self.server_2.ef += 1

                next_time = self.tec2_distribution.generate() + self.clock
                new_event = event(2, 0, next_time, False)
                bisect.insort(self.lef, new_event)
                # TODO: statistics

    def finish(self):
        pass
        # TODO: gerar relatório
        # TODO: estatísticas finais
