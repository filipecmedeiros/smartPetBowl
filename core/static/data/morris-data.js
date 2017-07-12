$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '17:00:00 12/07/2017 Q1',
            Nivel: 4
        }, 
        {
            period: '17:05:00 12/07/2017 Q2',
            Nivel: 3
        },
        {
            period: '17:10:00 12/07/2017 Q3',
            Nivel: 2
        },
        {
            period: '17:15:00 12/07/2017 Q4',
            Nivel: 1
        },
        {
            period: '17:20:00 12/07/2017 Q5',
            Nivel: 4
        },
        {
            period: '17:25:00 12/07/2017 Q6',
            Nivel: 3
        },
        {
            period: '17:30:00 12/07/2017 Q7',
            Nivel: 1
        },
        {
            period: '17:35:00 12/07/2017 Q8',
            Nivel: 4
        },
        {
            period: '17:40:00 12/07/2017 Q9',
            Nivel: 3
        },
        {
            period: '17:45:00 12/07/2017 Q10',
            Nivel: 3
        },
        {
            period: '17:50:00 12/07/2017 Q11',
            Nivel: 2
        },
        {
            period: '17:00:00 12/07/2017 Q12',
            Nivel: 1
        }



        ],

        xkey: 'period',
        ykeys: ['Nivel'],
        labels: ['Nível do Reservatório'],
        pointSize: 1,
        hideHover: 'auto',
        resize: true
    });

    
    
});
