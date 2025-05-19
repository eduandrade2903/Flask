from flask import Flask, render_template, request, redirect, url_for
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def computerStatus():
    #Uso da CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    #Uso da Memoria
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    #Uso do Disco
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    #Uso da Rede
    network = psutil.net_io_counters()
    network_sent = network.bytes_sent
    network_recv = network.bytes_recv
    #Tempo de Atividade
    uptime = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_now = datetime.datetime.now()
    uptime_delta = uptime_now - uptime
    uptime_str = str(uptime_delta).split('.')[0] #remove os microssegundos
    #Processos ativos
    process = len(psutil.pids())


    return render_template(
        "index.html",
        title="Status do Computador",
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_usage=disk_usage,
        network_sent=network_sent,
        network_recv=network_recv,
        uptime=uptime_str,
        process=process
    )