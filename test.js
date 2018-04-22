var schedules = [[[['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']], [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']], [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]], 75];
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

var schedules3 = [[ [ [ '09:48', '12:26' ],
    [ '15:41', '15:59' ],
    [ '18:50', '18:57' ] ],
  [ [ '11:21', '12:42' ],
    [ '12:51', '13:20' ],
    [ '17:51', '17:53' ],
    [ '18:07', '18:11' ] ],
  [ [ '10:07', '10:39' ],
    [ '10:41', '11:03' ],
    [ '12:21', '12:22' ],
    [ '15:49', '16:11' ],
    [ '17:29', '17:54' ] ],
  [ [ '09:41', '09:57' ],
    [ '10:03', '10:14' ],
    [ '10:32', '10:39' ],
    [ '10:56', '11:17' ],
    [ '11:23', '11:41' ],
    [ '11:59', '12:03' ],
    [ '12:28', '12:45' ],
    [ '17:19', '17:27' ],
    [ '18:56', '18:57' ] ],
  [ [ '09:37', '11:19' ],
    [ '11:27', '13:37' ],
    [ '16:29', '17:41' ] ] ], 124];

function getStartTime(schedules, duration) {
    let cursor = Array.from({length: schedules.length}, _ => 0);
    let end = "09:00";

    function compare(endTime, _arr) {
        let c = 0;
        for (let a of _arr) {
            let range = a[cursor[c]];
            console.log(endTime, range);
            if (range && range[0] <= add(endTime, duration)) {
                cursor[c] += 1;
                return end = max(range[1], endTime)
            }
            c++;
        }
        return 1
    }

    function add(time, duration) {
        let time_arr = time.split(":");
        let m_p = parseInt(time_arr[1]) - 1 + duration;
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

    while (add(end, duration) <= "19:00") {
        let res = compare(end, schedules);
        if(res === 1) {
            return end
        }
    }
    return null
}
// console.log(getStartTime(...schedules2));
// console.log(getStartTime(...schedules));
console.log(getStartTime(...schedules3));
