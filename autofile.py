#一键生成报告
def pdf(png,txt):
    import time
    from reportlab.pdfbase import pdfmetrics   # 注册字体
    from reportlab.pdfbase.ttfonts import TTFont # 字体类
    from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
    from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
    from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
    from reportlab.lib import colors  # 颜色模块
    from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
    from reportlab.graphics.charts.legends import Legend  # 图例类
    from reportlab.graphics.shapes import Drawing  # 绘图工具
    from reportlab.lib.units import cm  # 单位：cm

    # 注册字体(提前准备好字体文件, 如果同一个文件需要多种字体可以注册多个)
    pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))

    class Graphs:
        # 绘制标题
        @staticmethod
        def draw_title(title: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 拿到标题样式
            ct = style['Heading1']
            # 单独设置样式相关属性
            ct.fontName = 'SimSun'      # 字体名
            ct.fontSize = 30          # 字体大小
            ct.leading = 50             # 行间距
            ct.textColor = colors.green     # 字体颜色
            ct.alignment = 1    # 居中
            ct.bold = True
            # 创建标题对应的段落，并且返回
            return Paragraph(title, ct)

      # 绘制小标题
        @staticmethod
        def draw_little_title(title: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 拿到标题样式
            ct = style['Normal']
            # 单独设置样式相关属性
            ct.fontName = 'SimSun'  # 字体名
            ct.fontSize = 15  # 字体大小
            ct.leading = 30  # 行间距
            ct.textColor = colors.red  # 字体颜色
            # 创建标题对应的段落，并且返回
            return Paragraph(title, ct)

        # 绘制普通段落内容
        @staticmethod
        def draw_text(text: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 获取普通样式
            ct = style['Normal']
            ct.fontName = 'SimSun'
            ct.fontSize = 12
            ct.wordWrap = 'CJK'     # 设置自动换行
            ct.alignment = 0        # 左对齐
            ct.firstLineIndent = 32     # 第一行开头空格
            ct.leading = 25
            return Paragraph(text, ct)

        # 绘制表格
        @staticmethod
        def draw_table(*args):
            # 列宽度
            col_width = 180
            style = [
                ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
                ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
                ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
                ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
                # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
                # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
                # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
                # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
            ]
            table = Table(args, colWidths=col_width, style=style)
            return table

        # 创建图表
        @staticmethod
        def draw_bar(bar_data: list, ax: list, items: list):
            drawing = Drawing(500, 250)
            bc = VerticalBarChart()
            bc.x = 45       # 整个图表的x坐标
            bc.y = 45      # 整个图表的y坐标
            bc.height = 200     # 图表的高度
            bc.width = 350      # 图表的宽度
            bc.data = bar_data
            bc.strokeColor = colors.black       # 顶部和右边轴线的颜色
            bc.valueAxis.valueMin = 0           # 设置y坐标的最小值
            bc.valueAxis.valueMax = 1         # 设置y坐标的最大值
            bc.valueAxis.valueStep = 0.05         # 设置y坐标的步长
            bc.categoryAxis.labels.dx = 2
            bc.categoryAxis.labels.dy = -8
            bc.categoryAxis.labels.angle = 20
            bc.categoryAxis.categoryNames = ax

            # 图示
            leg = Legend()
            leg.fontName = 'SimSun'
            leg.alignment = 'right'
            leg.boxAnchor = 'ne'
            leg.x = 475         # 图例的x坐标
            leg.y = 240
            leg.dxTextSpace = 10
            leg.columnMaximum = 3
            leg.colorNamePairs = items
            drawing.add(leg)
            drawing.add(bc)
            return drawing

        # 绘制图片
        @staticmethod
        def draw_img(path):
            img = Image(path)       # 读取指定路径下的图片
            img.drawWidth = 18*cm        # 设置图片的宽度
            img.drawHeight = 20*cm       # 设置图片的高度
            return img

    content = list()
    content.append(Graphs.draw_title('交通标志识别报告'))

    content.append(Graphs.draw_img(f'{png}'))
    with open(f'{txt}', 'r+', encoding='utf-8') as f:
        classes = f.readlines();  # speedlimit 0.0700 135 2 317 73
    speedlimit = 0
    speedlimit_score = 0
    crosswalk = 0
    crosswalk_score = 0
    trafficlight = 0
    trafficlight_score = 0
    stop = 0
    stop_score = 0
    for i in classes:
        spilt = i.split()
        if i.find('speedlimit') != -1:
            speedlimit += 1
            speedlimit_score += float(spilt[1])
        if i.find('crosswalk') != -1:
            crosswalk += 1
            crosswalk_score += float(spilt[1])
        if i.find('trafficlight') != -1:
            trafficlight += 1
            trafficlight_score += float(spilt[1])
        if i.find('stop') != -1:
            stop += 1
            stop_score += float(spilt[1])
    name = 0
    if speedlimit_score == max(speedlimit_score, crosswalk_score, trafficlight_score, stop_score):
        name = '限速标志'
    if speedlimit_score > 1:
        speedlimit_score = 1
    if crosswalk_score == max(speedlimit_score, crosswalk_score, trafficlight_score, stop_score):
        name = '人行道标志'
    if crosswalk_score > 1:
        crosswalk_score = 1
    if trafficlight_score == max(speedlimit_score, crosswalk_score, trafficlight_score, stop_score):
        name = '交通信号灯'
    if trafficlight_score > 1:
        trafficlight_score = 1
    if stop_score == max(speedlimit_score, crosswalk_score, trafficlight_score, stop_score):
        name = '停车标志'
    if stop_score > 1:
        stop_score = 1

    allbox = speedlimit + crosswalk + trafficlight + stop
    speedlimit_boxpie = speedlimit / allbox
    crosswalk_boxpie = crosswalk / allbox
    trafficlight_boxpie = trafficlight / allbox
    stop_boxpie = stop / allbox

    allscore = speedlimit_score + crosswalk_score + trafficlight_score + stop_score
    speedlimit_scorepie = speedlimit_score / allscore
    crosswalk_scorepie = crosswalk_score / allscore
    trafficlight_scorepie = trafficlight_score / allscore
    stop_scorepie = stop_score / allscore

    content.append(Graphs.draw_text(''))

    content.append(Graphs.draw_title('------------------------------'))
    content.append(Graphs.draw_little_title(f'鉴定为：{name}'))
    content.append(Graphs.draw_title('------------------------------'))

    databox = [
        ('类别', '预测框数量', '预测框占比'),
        ('限速标志', f'{speedlimit}', f'{speedlimit_boxpie*100:.2f}%'),
        ('人行道标志', f'{crosswalk}', f'{crosswalk_boxpie*100:.2f}%'),
        ('交通信号灯', f'{trafficlight}', f'{trafficlight_boxpie*100:.2f}%'),
        ('停车标志', f'{stop}', f'{stop_boxpie*100:.2f}%')
    ]
    content.append(Graphs.draw_table(*databox))

    content.append(Graphs.draw_title(''))
    content.append(Graphs.draw_little_title('可视化'))

    b_data = [(speedlimit_score, crosswalk_score, trafficlight_score, stop_score),
              (speedlimit_scorepie, crosswalk_scorepie, trafficlight_scorepie, stop_scorepie)]
    ax_data = ['speedlimit', 'crosswalk', 'trafficlight', 'stop']
    leg_items = [(colors.red, '预测框得分'), (colors.green, '预测框占比')]
    content.append(Graphs.draw_bar(b_data, ax_data, leg_items))

    content.append(Graphs.draw_title('------------------------------'))
    t =time.localtime()
    time=str(t.tm_year)+'年'+str( t.tm_mon)+'月'+str( t.tm_mday )+"日生成该报告"
    content.append(Graphs.draw_little_title(time))

    doc = SimpleDocTemplate('分析报告.pdf', pagesize=letter)
    doc.build(content)
    return 'finish'