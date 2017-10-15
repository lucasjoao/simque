document.getElementById('tec1').addEventListener('change', function () {
  var style = 'block';
  var ids = ['tec_c1', 'tec_n1', 'tec_u1', 'tec_t1', 'tec_e1'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('tec_c1').style.display = style;
      selected_id = 'tec_c1';
      break;
    case '1':
      document.getElementById('tec_n1').style.display = style;
      selected_id = 'tec_n1';
      break;
    case '2':
      document.getElementById('tec_u1').style.display = style;
      selected_id = 'tec_u1';
      break;
    case '3':
      document.getElementById('tec_t1').style.display = style;
      selected_id = 'tec_t1';
      break;
    case '4':
      document.getElementById('tec_e1').style.display = style;
      selected_id = 'tec_e1';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});

document.getElementById('tec2').addEventListener('change', function () {
  var style = 'block';
  var ids = ['tec_c2', 'tec_n2', 'tec_u2', 'tec_t2', 'tec_e2'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('tec_c2').style.display = style;
      selected_id = 'tec_c2';
      break;
    case '1':
      document.getElementById('tec_n2').style.display = style;
      selected_id = 'tec_n2';
      break;
    case '2':
      document.getElementById('tec_u2').style.display = style;
      selected_id = 'tec_u2';
      break;
    case '3':
      document.getElementById('tec_t2').style.display = style;
      selected_id = 'tec_t2';
      break;
    case '4':
      document.getElementById('tec_e2').style.display = style;
      selected_id = 'tec_e2';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});

document.getElementById('ts1').addEventListener('change', function () {
  var style = 'block';
  var ids = ['ts_c1', 'ts_n1', 'ts_u1', 'ts_t1', 'ts_e1'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('ts_c1').style.display = style;
      selected_id = 'ts_c1';
      break;
    case '1':
      document.getElementById('ts_n1').style.display = style;
      selected_id = 'ts_n1';
      break;
    case '2':
      document.getElementById('ts_u1').style.display = style;
      selected_id = 'ts_u1';
      break;
    case '3':
      document.getElementById('ts_t1').style.display = style;
      selected_id = 'ts_t1';
      break;
    case '4':
      document.getElementById('ts_e1').style.display = style;
      selected_id = 'ts_e1';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});

document.getElementById('ts2').addEventListener('change', function () {
  var style = 'block';
  var ids = ['ts_c2', 'ts_n2', 'ts_u2', 'ts_t2', 'ts_e2'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('ts_c2').style.display = style;
      selected_id = 'ts_c2';
      break;
    case '1':
      document.getElementById('ts_n2').style.display = style;
      selected_id = 'ts_n2';
      break;
    case '2':
      document.getElementById('ts_u2').style.display = style;
      selected_id = 'ts_u2';
      break;
    case '3':
      document.getElementById('ts_t2').style.display = style;
      selected_id = 'ts_t2';
      break;
    case '4':
      document.getElementById('ts_e2').style.display = style;
      selected_id = 'ts_e2';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});

document.getElementById('tef').addEventListener('change', function () {
  var style = 'block';
  var ids = ['tef_c', 'tef_n', 'tef_u', 'tef_t', 'tef_e'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('tef_c').style.display = style;
      selected_id = 'tef_c';
      break;
    case '1':
      document.getElementById('tef_n').style.display = style;
      selected_id = 'tef_n';
      break;
    case '2':
      document.getElementById('tef_u').style.display = style;
      selected_id = 'tef_u';
      break;
    case '3':
      document.getElementById('tef_t').style.display = style;
      selected_id = 'tef_t';
      break;
    case '4':
      document.getElementById('tef_e').style.display = style;
      selected_id = 'tef_e';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});

document.getElementById('tf').addEventListener('change', function () {
  var style = 'block';
  var ids = ['tf_c', 'tf_n', 'tf_u', 'tf_t', 'tf_e'];
  var selected_id;
  switch (this.value) {
    case '0':
      document.getElementById('tf_c').style.display = style;
      selected_id = 'tf_c';
      break;
    case '1':
      document.getElementById('tf_n').style.display = style;
      selected_id = 'tf_n';
      break;
    case '2':
      document.getElementById('tf_u').style.display = style;
      selected_id = 'tf_u';
      break;
    case '3':
      document.getElementById('tf_t').style.display = style;
      selected_id = 'tf_t';
      break;
    case '4':
      document.getElementById('tf_e').style.display = style;
      selected_id = 'tf_e';
      break;
    default:
      break;
  }
  for (i = 0; i < ids.length; i++) {
    if (selected_id != ids[i])
      document.getElementById(ids[i]).style.display = 'none';
  }
});


