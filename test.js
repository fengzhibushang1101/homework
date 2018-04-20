var schedules = [[[['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']], [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']], [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]], 76];
var schedules2 = [
    [ [ [ '09:00', '11:30' ],
    [ '13:30', '16:00' ],
    [ '16:00', '17:30' ],
    [ '17:45', '19:00' ] ],
  [ [ '09:15', '12:00' ],
    [ '14:00', '16:30' ],
    [ '17:00', '17:30' ] ],
  [ [ '11:30', '12:15' ],
    [ '15:00', '16:30' ],
    [ '17:45', '19:00' ] ] ], 60
];


function getStartTime(schedules, duration) {
    let cursor = [0,0,0];
    let _end = "09:00";

    function compare(endTime, _arr) {
        let c = 0;
        for (let a of _arr) {
            let range = a[cursor[c]];
            if (range) {
                if (range[0] < add(endTime, duration)) {
                    cursor[c] += 1;
                    return _end = max(range[1], endTime)
                }
            } else {
                return 0
            }
            c++;
        }
        return 1
    }

    function add(time, duration) {
        let time_arr = time.split(":");
        let m_p = parseInt(time_arr[1]) + duration;
        let extra = Math.floor(m_p / 60);
        let f_m = m_p % 60;
        let h_str = (parseInt(time_arr[0]) + extra).toString();
        let m_str = f_m.toString();
        return `${ h_str.length > 1? h_str: "0" + h_str }:${ m_str.length > 1? m_str: "0" + m_str }`
    }

    function max(...rest) {
        let max = "0";
        rest.forEach(v => {
            if (v > max) {
                max = v;
            }
        });
        return max
    }

    while (true) {
        let res = compare(_end, schedules);
        switch (res) {
            case 1:
                return _end;
            case 0:
                return null;
            default:
                break;
        }
    }
}
console.log(getStartTime(...schedules2));
console.log(getStartTime(...schedules));
