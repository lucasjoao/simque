

class statistics(object):

    def __init__(self):
        self.change_ent_1 = 0
        self.change_ent_2 = 0

        self.fail_time_srv_1 = 0
        self.fail_time_srv_2 = 0
        self.fails_srv_1 = 0
        self.fails_srv_2 = 0
        self.fail_time_percentual_srv_1 = 0.0
        self.fail_time_percentual_srv_2 = 0.0

        # TODO: solucao da tela de simulacao impacta nas proximas est.
        self.count_end_ent_1 = 0
        self.count_end_ent_2 = 0
        self.count_start_ent_1 = 0
        self.count_start_ent_2 = 0
        self.count_in_sim_ent_1 = 0
        self.count_in_sim_ent_2 = 0
        # ---------------------------------------------------------------------

        self.total_time_ent_1 = 0
        self.total_time_ent_2 = 0
        self.avrg_time_ent_1 = 0.0
        self.avrg_time_ent_2 = 0.0

        self.total_queue = 0
        self.total_queue_time = 0
        self.avrg_queue_time = 0.0

    def last_values(self, clock):
        self.fail_time_percentual_srv_1 = (self.fail_time_srv_1 * 100) / clock
        self.fail_time_percentual_srv_2 = (self.fail_time_srv_2 * 100) / clock

        # TODO: solucao da tela de simulacao impacta nas proximas est.
        self.avrg_time_ent_1 = self.total_time_ent_1 / self.count_end_ent_1
        self.avrg_time_ent_2 = self.total_time_ent_2 / self.count_end_ent_2
        # ---------------------------------------------------------------------

        self.avrg_queue_time = self.total_queue_time / self.total_queue
