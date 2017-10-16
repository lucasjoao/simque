

class simulator(object):

    def __init__(self, form):
        self.limit_queue = form['limit_queue']

        if form['tec1_aleatory'] == '0':
            self.tec1_const_media = form['tec_c1']
        elif form['tec1_aleatory'] == '1':
            self.tec1_const_media = form['tec_n_media1']
            self.tec1_dp_moda = form['tec_n_dp1']
        elif form['tec1_aleatory'] == '2':
            self.tec1_min = form['tec_u_min1']
            self.tec1_max = form['tec_u_max1']
        elif form['tec1_aleatory'] == '3':
            self.tec1_dp_moda = form['tec_t_mod1']
            self.tec1_min = form['tec_t_min1']
            self.tec1_max = form['tec_t_max1']
        elif form['tec1_aleatory'] == '4':
            self.tec1_const_media = form['tec_e1']

        if form['tec2_aleatory'] == '0':
            self.tec2_const_media = form['tec_c2']
        elif form['tec2_aleatory'] == '1':
            self.tec2_const_media = form['tec_n_media2']
            self.tec2_dp_moda = form['tec_n_dp2']
        elif form['tec2_aleatory'] == '2':
            self.tec2_min = form['tec_u_min2']
            self.tec2_max = form['tec_u_max2']
        elif form['tec2_aleatory'] == '3':
            self.tec2_dp_moda = form['tec_t_mod2']
            self.tec2_min = form['tec_t_min2']
            self.tec2_max = form['tec_t_max2']
        elif form['tec2_aleatory'] == '4':
            self.tec2_const_media = form['tec_e2']

        if form['ts1_aleatory'] == '0':
            self.ts1_const_media = form['ts_c1']
        elif form['ts1_aleatory'] == '1':
            self.ts1_const_media = form['ts_n_media1']
            self.ts1_dp_moda = form['ts_n_dp1']
        elif form['ts1_aleatory'] == '2':
            self.ts1_min = form['ts_u_min1']
            self.ts1_max = form['ts_u_max1']
        elif form['ts1_aleatory'] == '3':
            self.ts1_dp_moda = form['ts_t_mod1']
            self.ts1_min = form['ts_t_min1']
            self.ts1_max = form['ts_t_max1']
        elif form['ts1_aleatory'] == '4':
            self.ts1_const_media = form['ts_e1']

        if form['ts2_aleatory'] == '0':
            self.ts2_const_media = form['ts_c2']
        elif form['ts2_aleatory'] == '1':
            self.ts2_const_media = form['ts_n_media2']
            self.ts2_dp_moda = form['ts_n_dp2']
        elif form['ts2_aleatory'] == '2':
            self.ts2_min = form['ts_u_min2']
            self.ts2_max = form['ts_u_max2']
        elif form['ts2_aleatory'] == '3':
            self.ts2_dp_moda = form['ts_t_mod2']
            self.ts2_min = form['ts_t_min2']
            self.ts2_max = form['ts_t_max2']
        elif form['ts2_aleatory'] == '4':
            self.ts2_const_media = form['ts_e2']

        if form['tef_aleatory'] == '0':
            self.tef_const_media = form['tef_c']
        elif form['tef_aleatory'] == '1':
            self.tef_const_media = form['tef_n_media']
            self.tef_dp_moda = form['tef_n_dp']
        elif form['tef_aleatory'] == '2':
            self.tef_min = form['tef_u_min']
            self.tef_max = form['tef_u_max']
        elif form['tef_aleatory'] == '3':
            self.tef_dp_moda = form['tef_t_mod']
            self.tef_min = form['tef_t_min']
            self.tef_max = form['tef_t_max']
        elif form['tef_aleatory'] == '4':
            self.tef_const_media = form['tef_e']

        if form['tf_aleatory'] == '0':
            self.tf_const_media = form['tf_c']
        elif form['tf_aleatory'] == '1':
            self.tf_const_media = form['tf_n_media']
            self.tf_dp_moda = form['tf_n_dp']
        elif form['tf_aleatory'] == '2':
            self.tf_min = form['tf_u_min']
            self.tf_max = form['tf_u_max']
        elif form['tf_aleatory'] == '3':
            self.tf_dp_moda = form['tf_t_mod']
            self.tf_min = form['tf_t_min']
            self.tf_max = form['tf_t_max']
        elif form['tf_aleatory'] == '4':
            self.tf_const_media = form['tf_e']

    def start(self):
        self.clock = 0
        self.lef = []
        # variaveis de estado, contadores, estatisticas

    def next_time(self):
        pass

    def event(self):
        pass

    def finish(self):
        pass
