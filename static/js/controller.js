/*
函数：get_map_data
参数：无
作用：提取数据库数据，通过ajax异步载入到HTML页面
变量释义：
  map_option：地图的option配置对象
  res：从数据库按要求提取的数据
  map：echarts初始化后生成的对象
 */
function get_map_data() {
    $.ajax({
        // ajax执行的路由地址
        url: '/map',

        /*
        成功访问路由地址时，运行如下函数，参数为res
        将提取的数据分类别赋值给option.series.data，提供页面显示数据
         */
        success: function(res) {
            map_option.series[0].data=res.total_nums  //总人数
            map_option.series[1].data=res.man_nums    //男生人数
            map_option.series[2].data=res.man_names   //所有男生名字
            map_option.series[3].data=res.woman_nums  //女生人数
            map_option.series[4].data=res.woman_names //所有女生名字
            map.setOption(map_option)           //echarts对象设置修改后的option配置，完成数据供应
        },
        //不成功访问路由地址，不进行操作
        error: function(xhr, type, errorThrown) {

        }
    })
}

//运行函数，向页面提交数据
get_map_data()