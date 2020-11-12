// 获取echarts初始化对象
var map = echarts.init(document.getElementById('map'), "dark");

// 自定义地图的option配置
var map_option = {
    // 地图标题
    title: {
        text: '学生信息',
        subtext: '',
        left: 'center'
    },
    // 鼠标放在指定省份上显示的信息
    tooltip: {
        trigger: 'item',
        // 按照series的顺序输出相关信息
        formatter: function (params) {
            // 第一行显示每个省份的名字
            var res = params.name + '<br/>';
            // 获取option里的series
            var myseries = map_option.series;
            // 遍历每个series，将每一个series数据逐行输出
            for (var i = 0; i < myseries.length; i++) {
                for (var j = 0; j < myseries[i].data.length; j++) {
                    if (myseries[i].data[j].name == params.name) {
                        res += myseries[i].name + ' : ' + myseries[i].data[j].value + '</br>';
                    }
                }
            }
            return res;
        },
        // 使显示的信息不超出边界
        confine: true
    },
    // 自定义地图左侧的数值标签
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 2, end: 10 },
        { start: 10, end: 20 },
        { start: 20, end: 30 },
        { start: 30, end: 40 },
        { start: 40 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1'],
        formatter: function (value) {
            switch (value) {
                case 2:
                    return '1 - 5'
                case 10:
                    return '5 - 10'
                case 20:
                    return '10 - 15'
                case 30:
                    return '15 - 20'
                case 40:
                    return '> 20'
            }
        }
    },
    //配置数据
    series: [
        {
            name: '学生人数',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            // 左侧小导航图标
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            tooltip: {
                show: true
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 10,
                    color: '#111111'
                },
                emphasis: {
                    show: true,
                    fontSize: 8,
                }
            },
            data: []  //数据
        },
        {
            name: '男生人数',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            tooltip: {
                show: true
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 10,
                    color: '#111111'
                },
                emphasis: {
                    show: true,
                    fontSize: 8,
                }
            },
            data: [],  //数据
        },
        {
            name: '男生',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            tooltip: {
                show: true
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 10,
                    color: '#111111'
                },
                emphasis: {
                    show: true,
                    fontSize: 8,
                }
            },
            data: [],  //数据
        },
        {
            name: '女生人数',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            // 左侧小导航图标
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            tooltip: {
                show: true
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 10,
                    color: '#111111'
                },
                emphasis: {
                    show: true,
                    fontSize: 8,
                }
            },
            data: []  //数据
        },
        {
            name: '女生',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            tooltip: {
                show: true
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 10,
                    color: '#111111'
                },
                emphasis: {
                    show: true,
                    fontSize: 8,
                }
            },
            data: [],  //数据
        }]
};

// 向地图配置option
map.setOption(map_option)