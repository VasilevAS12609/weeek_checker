colour_main = "#2F5496"
colour_red = "red"
task_num = ""
task_text = ""
ait_exec = ""
ait_bt = ""
ait_volume = ""
task_status = ""
step_exec = ""
step_date = ""

html = f"""
<html>
    <body style='font-style: Calibri;font-size: 12.0pt;color: {colour_main}'>
        <div>
            <p>
                <b><u><span>ЗнИ: </span></u></b>
                <span>{task_text}</span><br>
                
                <b><u><span'>АИТ: </span></u></b>
                <span>{ait_exec} | <b><u>БТ –</u></b> {ait_bt} | <b><u>Объем &#8211;</u></b> {ait_volume} ч/ч</span><br>
                
                <b><u><span>Статус: </span></u></b>
                <span>{task_status}</span><br>
                
                <b><u><span>Отв. за этап: </span></u></b>
                <span>{step_exec} | <b><u>Срок по этапу: </u></b> {step_date}</span>
            </p>
        </div>
    </body>
</html>
"""
