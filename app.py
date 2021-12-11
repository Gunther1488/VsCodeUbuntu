import psutil
def get_cpu():
    data = {}
    data.update(
        cpu_time = psutil.cpu_times(),
        cpu_perc = psutil.cpu_percent(),
        cpu_stat = psutil.cpu_stats(),
        cpu_frek = psutil.cpu_freq(),
        )
    return data
def get_network():
    data = {}
    data.update(
        net_stat = psutil.net_if_stats(),
    )
    return data

def get_memory():
    data = {}
    data.update(
        vir_memo = psutil.virtual_memory(),
        swp_memo = psutil.swap_memory(),
    )
    return data

def show(**kwargs):
    print("||||||||||||||||||||||||||||||||||||||||||||||||||")
    cpu_info = "cpu_time: {cpu_time}|||  cpu_perc: {cpu_perc}|||  cpu_stat: {cpu_stat}|||  cpu_frek: {cpu_frek}|||"
    print(cpu_info.format(**kwargs['cpu']))
    network_info = ">>><<< net_stat: {}>>><<<"
    print(network_info.format(kwargs["network"]["net_stat"]))
    memory_info = "vir_memo: {} --- swp_memo {}---"
    print(memory_info.format(kwargs["memory"]["vir_memo"], kwargs["memory"]["swp_memo"]))
    print("||||||||||||||||||||||||||||||||||||||||||||||||||")

def run():
    cpu = get_cpu()
    network = get_network()
    memory = get_memory()
    show(cpu = cpu, network = network, memory = memory)

if __name__ == "__main__":
    run()