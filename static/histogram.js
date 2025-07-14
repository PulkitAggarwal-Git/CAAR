console.log("Loaded");

document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('tag_count_chart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: window.chartLabels,
            datasets: [{
                label: 'Tag Frequency',
                data: window.chartData,
                backgroundColor: 'steelblue'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    ticks: {
                        color: 'white'
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: 'white'
                    }
                }
            }
        }
    });
});