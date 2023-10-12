import datetime
import time


def html_draft(task_text, step_date):
    colour_main = "#2F5496"
    colour_red = "red"
    step_date_colour = colour_main
    task_num = "Нет данных"
    # task_text = "Нет данных"
    ait_exec = "Нет данных"
    ait_bt = "Нет данных"
    ait_volume = "Нет данных"
    task_status = "Нет данных"
    step_exec = "Нет данных"
    step_date = datetime.datetime.strptime(step_date, '%d.%m.%Y').date()

    warn_teg_open = ""
    warn_teg_close = ""
    if step_date <= datetime.datetime.now().date():
        step_date_colour = colour_red
        warn_teg_open = f"<b><u><font color={step_date_colour}>"
        warn_teg_close = f"</font></u></b>"

    html_draft = f"""
    <html>
        <body style='font-style: Calibri;font-size: 12.0pt;color: {colour_main}'>
            <div>
                <p>
                    <b><u><span>ЗнИ:</span></u></b>
                    <span> {task_text}</span><br>
                    
                    <b><u><span'>АИТ:</span></u></b>
                    <span> {ait_exec} | <b><u>БТ</u></b> – {ait_bt} | <b><u>Объем</u></b> – {ait_volume} ч/ч</span><br>
                    
                    <b><u><span>Статус:</span></u></b>
                    <span> {task_status}</span><br>
                    
                    <b><u><span>Отв. за этап:</span></u></b>
                    <span> {step_exec} | <b><u>Срок по этапу:</u></b> {warn_teg_open}{step_date}{warn_teg_close}</span>
                </p>
            </div>
        </body>
    </html>
    <hr>
    """
    return html_draft
