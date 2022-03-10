$(function(){
    // 자동으로 ajax 실행
    $.ajax({
        url:"/fin/DailyCovid",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
                shapeChartData = {
                labels: data.intdate,
                datasets: [{
                    label: '코로나 확진자',
                    data: data.dailydecide,
                    borderColor: 'rosybrown',
                    backgroundColor: 'rosybrown',
                    borderWidth: 4
                }]
            }
            barChart();
        },error:function(){
            alert("실패");
        }
    });
// id = radioBtn을 클릭했을 경우 실행
    $('#radioBtn').click(function () {
            // checked 상태의 radio의 값을 변수에 저장
            var radiovalue = $('input:radio[name=covid]:checked').val();
            // 해당 변수의 값이 무엇인가에 따라 다른 ajax 실행
            if(radiovalue == 'Total-Covid'){    
                $.ajax({
                url:"/fin/TotalCovid",
                type:"get",
                data:{},
                dataType:"json",
                success:function(data){
                        shapeChartData = {
                        labels: data.intdate,
                        datasets: [{
                            label: '코로나 확진자',
                            data: data.decideCnt,
                            borderColor: 'rosybrown',
                            backgroundColor: 'rosybrown',
                            borderWidth: 4
                        }]
                    }
                    barChart();
                },error:function(){
                    alert("실패");
                }
            })}else if(radiovalue == 'Daily-Covid'){
            $.ajax({
            url:"/fin/DailyCovid",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                    shapeChartData = {
                    labels: data.intdate,
                    datasets: [{
                        label: '코로나 확진자',
                        data: data.dailydecide,
                        borderColor: 'rosybrown',
                        backgroundColor: 'rosybrown',
                        borderWidth: 4
                    }]
                }
                barChart();
            },error:function(){
                alert("실패");
            }
        })}else if(radiovalue == 'Daily-Vaccine'){
            $.ajax({
            url:"/fin/DailyVaccine",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                    shapeChartData = {
                    labels: data.intdate,
                    datasets: [{
                        label: '1차백신 접종',
                        data: data.firstCnt,
                        borderColor: 'rosybrown',
                        backgroundColor: 'rosybrown',
                        borderWidth: 4},
                        {label: '2차 백신 접종',
                        data: data.secondCnt,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        borderWidth: 4},
                        {label: '3차 백신 접종',
                        data: data.thirdCnt,
                        borderColor: 'dark',
                        backgroundColor: 'gray',
                        borderWidth: 4
                    }]
                }
                barChart();
            },error:function(){
                alert("실패");
            }
        })}else if(radiovalue == 'Total-Vaccine'){
            $.ajax({
            url:"/fin/TotalVaccine",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                    shapeChartData = {
                    labels: data.intdate,
                    datasets: [{
                        label: '1차백신 누적 접종',
                        data: data.totalFirstCnt,
                        borderColor: 'rosybrown',
                        backgroundColor: 'rosybrown',
                        borderWidth: 4},
                        {label: '2차 백신 누적 접종',
                        data: data.totalSecondCnt,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        borderWidth: 4},
                        {label: '3차 백신 누적 접종',
                        data: data.totalThirdCnt,
                        borderColor: 'gray',
                        backgroundColor: 'gray',
                        borderWidth: 4
                    }]
                }
                barChart();
            },error:function(){
                alert("실패");
            }
        })}
    }) //id = radioBtn을 클릭했을 경우 실행 되는 함수
    //차트 그리기


    $("#fstock1btn").click(function(){
        var code = $("#fstock1").val()
        var radiovalue = $('input:radio[name=covid]:checked').val()
        if(radiovalue=='Daily-Covid'){   
            $.ajax({
                url:"/fin/code_DailyCovid",
                type:"GET",
                data:{'code':code},
                dataType:"json",
                success:function(data){
                    shapeChartData ={
                        labels: data.intdate,
                        datasets: [{
                        label: '2020-01-01종가 대비',
                        yAxisID: 'A',
                        data: data.codeclose,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        
                        }, {
                        label: '일일 신규 확진자',
                        yAxisID: 'B',
                        data: data.dailydecide,
                        borderColor: 'black',
                        backgroundColor: 'black',
                        }]
                    },
                    
                    chartOptions = {
                        responsive: true,
                        interaction: {
                        mode: 'index',
                        intersect: false,
                        },
                        stacked: false,
                        plugins: {
                        title: {
                            display: true,
                        }
                        },
                        scales: {
                        yAxes: [{
                            id: 'A',
                            type: 'linear',
                            display: true,
                            position: 'left',
                        }, {
                            id: 'B',
                            type: 'linear',
                            display: true,
                            position: 'right',
                        }]
                        }, grid: {
                            drawOnChartArea: false,
                        },
                    }
                    multiaxisChart();
                    // flist의 자식에 li 새로 추가하기
                    $("#flist").append("<li class='text'>" +  data.lowpoint  + data.lowrate  +  data.highpoint  +  data.highrate+"</li>");
                },error:function(){
                    alert("종목 코드를 다시 확인해주세요");
                }
            })
        }else if(radiovalue=='Total-Covid'){
            $.ajax({
                url:"/fin/code_totalCovid",
                type:"GET",
                data:{'code':code},
                dataType:"json",
                success:function(data){
                    shapeChartData ={
                        labels: data.intdate,
                        datasets: [{
                        label: '2020-01-01종가 대비',
                        yAxisID: 'A',
                        data: data.codeclose,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        
                        }, {
                        label: '누적 확진자',
                        yAxisID: 'B',
                        data: data.decideCnt,
                        borderColor: 'black',
                        backgroundColor: 'black',
                        }]
                    },
                    
                    chartOptions = {
                        responsive: true,
                        interaction: {
                        mode: 'index',
                        intersect: false,
                        },
                        stacked: false,
                        plugins: {
                        title: {
                            display: true,
                        }
                        },
                        scales: {
                        yAxes: [{
                            id: 'A',
                            type: 'linear',
                            display: true,
                            position: 'left',
                        }, {
                            id: 'B',
                            type: 'linear',
                            display: true,
                            position: 'right',
                        }]
                        }, 

                    }
                    multiaxisChart();
                    $("#flist").append("<li class='text'>" +  data.lowpoint  + data.lowrate  +  data.highpoint  +  data.highrate+"</li>");
                },error:function(){
                    alert("종목 코드를 다시 확인해주세요");
                }
            })

        }else if(radiovalue=='Total-Vaccine'){
            $.ajax({
                url:"/fin/code_totalVaccine",
                type:"GET",
                data:{'code':code},
                dataType:"json",
                success:function(data){
                    shapeChartData ={
                        labels: data.intdate,
                        datasets: [{
                        label: '2020-01-01종가 대비',
                        yAxisID: 'A',
                        data: data.codeclose,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        
                        }, {
                        label: '누적 1차 백신 접종자',
                        yAxisID: 'B',
                        data: data.totalFirstCnt,
                        borderColor: 'black',
                        backgroundColor: 'black',
                        },{
                        label: '누적 2차 백신 접종자',
                        yAxisID: 'B',
                        data: data.totalSecondCnt,
                        borderColor: 'gray',
                        backgroundColor: 'gray',
                        },{
                        label: '누적 3차 백신 접종자',
                        yAxisID: 'B',
                        data: data.totalThirdCnt,
                        borderColor: 'silver',
                        backgroundColor: 'silver',
                        }]
                    },
                    
                    chartOptions = {
                        responsive: true,
                        interaction: {
                        mode: 'index',
                        intersect: false,
                        },
                        stacked: false,
                        plugins: {
                        title: {
                            display: true,
                        }
                        },
                        scales: {
                        yAxes: [{
                            id: 'A',
                            type: 'linear',
                            display: true,
                            position: 'left',
                        }, {
                            id: 'B',
                            type: 'linear',
                            display: true,
                            position: 'right',
                        }]
                        }, grid: {
                            drawOnChartArea: false, 
                        },
                    }
                    multiaxisChart();
                    $("#flist").append("<li class='text'>" +  data.lowpoint  + data.lowrate  +  data.highpoint  +  data.highrate+"</li>");
                },error:function(){
                    alert("종목 코드를 다시 확인해주세요");
                }
            })

        }else if(radiovalue=='Daily-Vaccine'){
            $.ajax({
                url:"/fin/code_dailyVaccine",
                type:"GET",
                data:{'code':code, 'radiovalue':radiovalue},
                dataType:"json",
                success:function(data){
                    shapeChartData ={
                        labels: data.intdate,
                        datasets: [{
                        label: '2020-01-01종가 대비',
                        yAxisID: 'A',
                        data: data.codeclose,
                        borderColor: 'brown',
                        backgroundColor: 'brown',
                        
                        }, {
                        label: '일일 1차 백신 접종자',
                        yAxisID: 'B',
                        data: data.firstCnt,
                        borderColor: 'black',
                        backgroundColor: 'black',
                        },{
                        label: '일일 2차 백신 접종자',
                        yAxisID: 'B',
                        data: data.secondCnt,
                        borderColor: 'gray',
                        backgroundColor: 'gray',
                        },{
                        label: '일일 3차 백신 접종자',
                        yAxisID: 'B',
                        data: data.thirdCnt,
                        borderColor: 'silver',
                        backgroundColor: 'silver',
                        }]
                    },
                    
                    chartOptions = {
                        responsive: true,
                        interaction: {
                        mode: 'index',
                        intersect: false,
                        },
                        stacked: false,
                        plugins: {
                        title: {
                            display: true,
                        }
                        },
                        scales: {
                        yAxes: [{
                            id: 'A',
                            type: 'linear',
                            display: true,
                            position: 'left',
                        }, {
                            id: 'B',
                            type: 'linear',
                            display: true,
                            position: 'right',
                        }]
                        }, grid: {
                            drawOnChartArea: false, 
                        },
                    }
                    multiaxisChart();
                    $("#flist").append("<li class='text'>" +  data.lowpoint  + data.lowrate  +  data.highpoint  +  data.highrate+"</li>");
                },error:function(){
                    alert("종목 코드를 다시 확인해주세요");
                }
            })

        }  
        
        })
    //fstock2btn이 클릭 됐을 때 작동
    $("#fstock2btn").click(function(){
        // fstock2의 값 가져오기
        var code = $("#fstock2").val()
        // fstock3의 값 가져오기
        var date = $("#fstock3").val()
        $.ajax({
            url:"/fin/codeDate",
            type:"get",
            // 받아온 값들을 views의 request로 보내기
            data:{'code':code, 'date':date},
            dataType:"json",
            success:function(data){
                // alert(data.percent['rate'])
                shapeChartData ={
                    labels: data.percent['Date'],
                    datasets: [{
                    label: '2020-01-01종가 대비',
                    yAxisID: 'A',
                    data: data.percent['Change'],
                    borderColor: 'black',    
                    backgroundColor: "rosybrown",            
                    }]
                },
                chartOptions = {
                    responsive: true,
                    interaction: {
                    mode: 'index',
                    intersect: false,
                    },
                    stacked: false,
                    plugins: {
                    title: {
                        display: true,
                    }
                    },
                    scales: {
                    yAxes: [{
                        id: 'A',
                        type: 'linear',
                        display: true,
                        position: 'left',
                    }]
                    }, 
                }
                multiaxisChart();
                $("#flist").append("<li class='text'> " +'해당 날짜의 코로나 신규 확진자는 전일 대비 ' +  data.percent['covidrate'] + '% 증감했습니다.   <br> 코로나 신규 확진자의 증감율이 ' + data.percent['changePerfloor']*100 +'%와' +  data.percent['changePerceil']*100  + '% 사이 구간인 경우 해당 종목은 ' + data.percent['rate'] + '%의 확률로 상승했습니다. <br>   위의 그래프는, 코로나의 신규확진자 추세가 ' +data.percent['changePerfloor']*100 +'%와' +  data.percent['changePerceil']*100 +'% 사이인 경우의 주가 증감율을 나타냅니다.'
                +"</li>")
            },
            error:function(){
                alert("실패");
            }
        })
    })


// fresetbnt 클릭 식 작동
    $("#fresetbnt").click(function(){
        // flist를 삭제
        $('#flist').remove(); 
        // id ftext 자식으로 <ul id="flist"><li></li></ul> 생성
        $('#ftext').append('<ul id="flist"><li></li></ul>');
    })

    $("#radioBtn2").click(function(){
        var date = $("#fcovid1").val()
        $.ajax({
            url:"/fin/covidspread",
            type:"get",
            data:{'date':date},
            dataType:"json",
            success:function(data){
                $("#flist").append("<li class='text'> 전국 코로나 확진율 : "+data.spread['tocovidPer']+" 지난 7일 평균 코로나 확진자 대비 확진자 증감률: "+data.spread['covidCompare']+"%</li>")
            },
            error:function(){
                alert("실패");
            }
        
        })
    })


})


function barChart() {
    // id myChart의 html 삭제
    $('#myChart').remove(); 
    // id fchart의 자식으로 <canvas id="myChart"><canvas> 생성
    $('#fchart').append('<canvas id="myChart"></canvas>');
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: shapeChartData,
        options:  {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}//createChart 

function multiaxisChart(){
    // id myChart의 html 삭제
    $('#myChart').remove(); 
    // id fchart의 자식으로 <canvas id="myChart"><canvas> 생성
    $('#fchart').append('<canvas id="myChart"></canvas>');
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: shapeChartData,
        options: chartOptions
    })
}