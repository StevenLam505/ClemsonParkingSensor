var lineChart;
const chart = document.getElementById('dayChart');

function CreateTable(){
  const newData = Array.from({length: 53}, () => Math.floor(Math.random() * 100));
  lineChart = new Chart(chart, {
  type: 'line',
  data: {
    labels: ['7:00 AM', '7:15 AM', '7:30 AM', '7:45 AM', 
    '8:00 AM', '8:15 AM', '8:30 AM', '8:45 AM', 
    '9:00 AM', '9:15 AM', '9:30 AM', '9:45 AM', 
    '10:00 AM', '10:15 AM', '10:30 AM', '10:45 AM', 
    '11:00 AM', '11:15 AM', '11:30 AM', '11:45 AM', 
    '12:00 PM', '12:15 PM', '12:30 PM', '12:45 PM', 
    '1:00 PM', '1:15 PM', '1:30 PM', '1:45 PM', 
    '2:00 PM', '2:15 PM', '2:30 PM', '2:45 PM', 
    '3:00 PM', '3:15 PM', '3:30 PM', '3:45 PM', 
    '4:00 PM', '4:15 PM', '4:30 PM', '4:45 PM', 
    '5:00 PM', '5:15 PM', '5:30 PM', '5:45 PM', 
    '6:00 PM', '6:15 PM', '6:30 PM', '6:45 PM', 
    '7:00 PM', '7:15 PM', '7:30 PM', '7:45 PM', 
    '8:00 PM'],
    datasets: [{
      label: 'Percent At Capacity',
      data: retrieveData(),
      borderWidth: 1,
      backgroundColor: '#F56600',
      borderColor: '#F56600'
    }]},
    options: {
      scales: {
        y: {
          beginAtZero: true,
          min: 0,
          max: 100
        }
      },
      responsive: true
    }
  });
}

function ChangeParkingLot(){
  let result = objArray.map(hc_data => hc_data.foo);
  console.log(result);
  lineChart.destroy();
  CreateTable();
}