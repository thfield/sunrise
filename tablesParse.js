const fs = require('fs')
const path = require('path')

let files = [
    '2020-07.tsv',
    '2020-08.tsv',
    '2020-09.tsv',
    '2020-10.tsv',
    '2020-11.tsv',
    '2020-12.tsv',
    '2021-01.tsv',
    '2021-02.tsv',
    '2021-03.tsv',
    '2021-04.tsv',
    '2021-05.tsv',
    '2021-06.tsv',
    '2021-07.tsv',
    '2021-08.tsv',
    '2021-09.tsv',
    '2021-10.tsv',
    '2021-11.tsv',
    '2021-12.tsv',
]

function replaceStrings(tsv, yearMonth) {
    let replaceRe = [
        [/ ↑/g, ''],
        [/−/g, '-'],
        [/^1\t/, `${yearMonth}-01\t`],
        [/\n(\d\d)\t/g, `\n${yearMonth}-$1\t`],
        [/\n(\d)\t/g, `\n${yearMonth}-0$1\t`],
        [/\b(\d:\d\d) am/g, '0$1'],
        [/\b(\d\d:\d\d) am/g, '$1'],
        [/12(:\d\d) pm/g,'12$1'],
        [/1(:\d\d) pm/g,'13$1'],
        [/4(:\d\d) pm/g,'16$1'],
        [/5(:\d\d) pm/g,'17$1'],
        [/6(:\d\d) pm/g,'18$1'],
        [/7(:\d\d) pm/g,'19$1'],
        [/8(:\d\d) pm/g,'20$1'],
        [/9(:\d\d) pm/g,'21$1'],
        [/10(:\d\d) pm/g,'22$1'],
        [/11(:\d\d) pm/g,'23$1'],
        [/\t/g, ','],
    ]
    replaceRe.forEach((ex) => {
        tsv = tsv.replace(ex[0], ex[1])
    })
    return tsv
}

let final = [
    'Date,Sunrise,Sunset,Daylength,DaylengthDiff,AstTwiStart,AstTwiEnd,NauTwiStart,NauTwiEnd,CivTwiStart,CivTwiEnd,SolNoon,SolNoonMilMi'
]
for (let file of files) {
    let data = fs.readFileSync(`tables/${file}`, {encoding: 'utf8'})
    let yearMonth = path.basename(file, '.tsv')
    data = replaceStrings(data, yearMonth)
    
    final.push(data)
}
fs.writeFileSync('data/timeanddate.csv', final.join('\n'))