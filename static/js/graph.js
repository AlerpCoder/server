var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    label: 'Temp',
                    data: temp_data,
                    borderColor: "rgba(255,0,0,0.6)",
                    backgroundColor: "rgba(255,0,0,0.5)",
                    pointBackgroundColor: "rgba(255,0,0,0.5)",
                    fill: false
                },
                {
                    label: 'Hum',
                    data: hum_data,
                    borderColor: "rgba(0,0,255,0.6)",
                    backgroundColor: "rgba(0,0,255,0.5)",
                    pointBackgroundColor: "rgba(0,0,255,0.5)",
                    fill: false
                }]
        },
    })
;