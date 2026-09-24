import os
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

# ----------------------------------------------------------------------
# 1) CONFIGURAÇÕES GERAIS
# ----------------------------------------------------------------------
PASTA_SAIDA = r"C:\Users\enzol\Downloads\graficos_forest_tabela_1_ponderada"
ROTULO_MEDIDA = "Prevalência (%)"
COR = "#1f7a4d"

# Cria a pasta caso não exista
os.makedirs(PASTA_SAIDA, exist_ok=True)

# ----------------------------------------------------------------------
# 2) DADOS DAS VARIÁVEIS (Tabela 1)
# ----------------------------------------------------------------------
VARIAVEIS = {
    "01_sexo": [
        {"header": "Sexo"},
        {
            "rotulo": "Feminino",
            "medida": 50.9,
            "li": 50.5,
            "ls": 51.2,
            "p": "< 0,001",
        },
        {
            "rotulo": "Masculino",
            "medida": 57.3,
            "li": 56.9,
            "ls": 57.8,
            "p": "—",
        },
    ],
    "02_estado_civil": [
        {"header": "Estado Civil"},
        {
            "rotulo": "Acompanhado",
            "medida": 61.8,
            "li": 61.4,
            "ls": 62.2,
            "p": "< 0,001",
        },
        {
            "rotulo": "Desacompanhado",
            "medida": 49.0,
            "li": 48.7,
            "ls": 49.3,
            "p": "—",
        },
    ],
    "03_cor_pele": [
        {"header": "Cor da Pele"},
        {
            "rotulo": "Amarela",
            "medida": 54.0,
            "li": 53.6,
            "ls": 54.4,
            "p": "< 0,001",
        },
        {
            "rotulo": "Branca",
            "medida": 52.9,
            "li": 52.5,
            "ls": 53.4,
            "p": "—",
        },
        {
            "rotulo": "Ignorada",
            "medida": 56.4,
            "li": 55.0,
            "ls": 57.8,
            "p": "—",
        },
        {
            "rotulo": "Indígena",
            "medida": 58.2,
            "li": 56.3,
            "ls": 60.0,
            "p": "—",
        },
        {
            "rotulo": "Negra",
            "medida": 55.0,
            "li": 54.2,
            "ls": 55.8,
            "p": "—",
        },
    ],
    "04_carne": [
        {"header": "Consumo de Carne"},
        {
            "rotulo": "< 5x/semana",
            "medida": 52.0,
            "li": 51.7,
            "ls": 52.4,
            "p": "0,003",
        },
        {
            "rotulo": "≥ 5x/semana",
            "medida": 51.0,
            "li": 50.4,
            "ls": 51.6,
            "p": "—",
        },
    ],
    "05_frango": [
        {"header": "Consumo de Frango"},
        {
            "rotulo": "< 5x/semana",
            "medida": 51.6,
            "li": 51.3,
            "ls": 52.0,
            "p": "0,071",
        },
        {
            "rotulo": "≥ 5x/semana",
            "medida": 52.4,
            "li": 51.6,
            "ls": 53.3,
            "p": "—",
        },
    ],
    "06_hortalicas_regular": [
        {"header": "Hortaliças Regular"},
        {
            "rotulo": "Não",
            "medida": 53.8,
            "li": 53.4,
            "ls": 54.1,
            "p": "0,725",
        },
        {
            "rotulo": "Sim",
            "medida": 53.9,
            "li": 53.5,
            "ls": 54.2,
            "p": "—",
        },
    ],
    "07_frutas_regular": [
        {"header": "Frutas Regular"},
        {
            "rotulo": "Não",
            "medida": 54.4,
            "li": 53.9,
            "ls": 54.8,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 53.4,
            "li": 53.1,
            "ls": 53.8,
            "p": "—",
        },
    ],
    "08_hortalicas_frutas_regular": [
        {"header": "Hortaliças e Frutas Regular"},
        {
            "rotulo": "Não",
            "medida": 54.0,
            "li": 53.6,
            "ls": 54.3,
            "p": "0,120",
        },
        {
            "rotulo": "Sim",
            "medida": 53.5,
            "li": 53.1,
            "ls": 54.0,
            "p": "—",
        },
    ],
    "09_bebidas_adocadas": [
        {"header": "Bebidas Adoçadas (≥ 5x/sem)"},
        {
            "rotulo": "Não",
            "medida": 54.1,
            "li": 53.8,
            "ls": 54.4,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 52.7,
            "li": 52.1,
            "ls": 53.4,
            "p": "—",
        },
    ],
    "10_troca_refeicao": [
        {"header": "Troca Refeição por Lanche"},
        {
            "rotulo": "Não",
            "medida": 52.9,
            "li": 52.5,
            "ls": 53.4,
            "p": "0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 54.7,
            "li": 53.7,
            "ls": 55.7,
            "p": "—",
        },
    ],
    "11_abuso_alcool": [
        {"header": "Consumo Abusivo de Álcool"},
        {
            "rotulo": "Não",
            "medida": 53.0,
            "li": 52.7,
            "ls": 53.3,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 57.5,
            "li": 56.8,
            "ls": 58.2,
            "p": "—",
        },
    ],
    "12_saude_ruim": [
        {"header": "Autoavaliação de Saúde Ruim"},
        {
            "rotulo": "Não",
            "medida": 53.2,
            "li": 52.9,
            "ls": 53.5,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 66.1,
            "li": 65.0,
            "ls": 67.2,
            "p": "—",
        },
    ],
    "13_insonia": [
        {"header": "Insônia"},
        {
            "rotulo": "Não",
            "medida": 61.5,
            "li": 60.1,
            "ls": 62.9,
            "p": "0,021",
        },
        {
            "rotulo": "Sim",
            "medida": 64.4,
            "li": 62.4,
            "ls": 66.4,
            "p": "—",
        },
    ],
    "14_plano_saude": [
        {"header": "Possui Plano de Saúde"},
        {
            "rotulo": "Não",
            "medida": 54.5,
            "li": 54.2,
            "ls": 54.9,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 52.9,
            "li": 52.6,
            "ls": 53.3,
            "p": "—",
        },
    ],
    "15_ultraprocessados": [
        {"header": "Consumo de Ultraprocessados"},
        {
            "rotulo": "Não",
            "medida": 57.9,
            "li": 57.3,
            "ls": 58.4,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 52.4,
            "li": 51.1,
            "ls": 53.8,
            "p": "—",
        },
    ],
    "16_anos_estudo": [
        {"header": "Anos de Estudo"},
        {
            "rotulo": "0 anos",
            "medida": 58.9,
            "li": 57.2,
            "ls": 60.6,
            "p": "< 0,001",
        },
        {
            "rotulo": "1 a 8 anos",
            "medida": 59.5,
            "li": 59.0,
            "ls": 60.0,
            "p": "—",
        },
        {
            "rotulo": "9 a 12 anos",
            "medida": 51.2,
            "li": 50.8,
            "ls": 51.7,
            "p": "—",
        },
        {
            "rotulo": "13+ anos",
            "medida": 50.5,
            "li": 50.0,
            "ls": 51.0,
            "p": "—",
        },
    ],
    "17_af_3meses": [
        {"header": "Atividade Física (Últimos 3 meses)"},
        {
            "rotulo": "Não",
            "medida": 55.4,
            "li": 55.0,
            "ls": 55.7,
            "p": "< 0,001",
        },
        {
            "rotulo": "Sim",
            "medida": 52.4,
            "li": 52.0,
            "ls": 52.7,
            "p": "—",
        },
    ],
    "18_af_1xsemana": [
        {"header": "Atividade Física (1x/semana)"},
        {
            "rotulo": "Não",
            "medida": 53.7,
            "li": 52.2,
            "ls": 55.3,
            "p": "0,073",
        },
        {
            "rotulo": "Sim",
            "medida": 52.3,
            "li": 51.9,
            "ls": 52.6,
            "p": "—",
        },
    ],
    "19_af_dias_semana": [
        {"header": "Atividade Física (Dias/semana)"},
        {
            "rotulo": "1 a 2 dias",
            "medida": 51.5,
            "li": 50.3,
            "ls": 52.7,
            "p": "< 0,001",
        },
        {
            "rotulo": "3 a 4 dias",
            "medida": 52.1,
            "li": 51.3,
            "ls": 52.8,
            "p": "—",
        },
        {
            "rotulo": "5 a 6 dias",
            "medida": 53.3,
            "li": 52.7,
            "ls": 53.9,
            "p": "—",
        },
        {
            "rotulo": "Todos os dias",
            "medida": 51.5,
            "li": 50.8,
            "ls": 52.2,
            "p": "—",
        },
    ],
    "20_af_duracao": [
        {"header": "Atividade Física (Duração)"},
        {
            "rotulo": "< 30 min",
            "medida": 52.4,
            "li": 50.7,
            "ls": 54.0,
            "p": "< 0,001",
        },
        {
            "rotulo": "30 a 59 min",
            "medida": 54.6,
            "li": 53.8,
            "ls": 55.4,
            "p": "—",
        },
        {
            "rotulo": "60+ min",
            "medida": 51.6,
            "li": 51.2,
            "ls": 52.1,
            "p": "—",
        },
    ],
    "21_tabagismo": [
        {"header": "Tabagismo"},
        {
            "rotulo": "Ex-fumante",
            "medida": 63.6,
            "li": 63.0,
            "ls": 64.2,
            "p": "< 0,001",
        },
        {
            "rotulo": "Fumante",
            "medida": 48.7,
            "li": 47.8,
            "ls": 49.6,
            "p": "—",
        },
        {
            "rotulo": "Nunca fumou",
            "medida": 52.5,
            "li": 52.2,
            "ls": 52.8,
            "p": "—",
        },
    ],
    "22_faixa_etaria": [
        {"header": "Faixa Etária"},
        {
            "rotulo": "18-24 anos",
            "medida": 30.5,
            "li": 29.9,
            "ls": 31.2,
            "p": "< 0,001",
        },
        {
            "rotulo": "25-34 anos",
            "medida": 49.7,
            "li": 49.1,
            "ls": 50.4,
            "p": "—",
        },
        {
            "rotulo": "35-44 anos",
            "medida": 59.6,
            "li": 59.0,
            "ls": 60.2,
            "p": "—",
        },
        {
            "rotulo": "45-54 anos",
            "medida": 62.5,
            "li": 61.9,
            "ls": 63.1,
            "p": "—",
        },
        {
            "rotulo": "55+ anos",
            "medida": 60.6,
            "li": 60.1,
            "ls": 61.0,
            "p": "—",
        },
    ],
    "23_regiao": [
        {"header": "Região"},
        {
            "rotulo": "Centro-Oeste",
            "medida": 52.2,
            "li": 51.7,
            "ls": 52.8,
            "p": "< 0,001",
        },
        {
            "rotulo": "Nordeste",
            "medida": 53.2,
            "li": 52.8,
            "ls": 53.5,
            "p": "—",
        },
        {
            "rotulo": "Norte",
            "medida": 55.2,
            "li": 54.8,
            "ls": 55.6,
            "p": "—",
        },
        {
            "rotulo": "Sudeste",
            "medida": 54.2,
            "li": 53.7,
            "ls": 54.7,
            "p": "—",
        },
        {
            "rotulo": "Sul",
            "medida": 54.4,
            "li": 53.8,
            "ls": 54.9,
            "p": "—",
        },
    ],
}
# ----------------------------------------------------------------------
# 3) FUNÇÕES AUXILIARES
# ----------------------------------------------------------------------


def fmt(x):
    """Formata número com 1 casa e vírgula decimal (padrão pt-BR)."""
    return f"{x:.1f}".replace(".", ",")


def texto_medida(d):
    return f"{fmt(d['medida'])} ({fmt(d['li'])} – {fmt(d['ls'])})"


def ticks_bonitos(xmin, xmax):
    candidatos = list(range(0, 101, 10))
    ticks = [t for t in candidatos if xmin <= t <= xmax]
    if not ticks:
        ticks = [int(xmin), int(xmax)]
    return ticks


# ----------------------------------------------------------------------
# 4) MONTAGEM E GERAÇÃO DOS GRÁFICOS
# ----------------------------------------------------------------------
def gerar_forest_plot(dados, caminho_arquivo):
    n = len(dados)
    for i, d in enumerate(dados):
        d["_y"] = n - i

    valores = []
    for d in dados:
        if "header" in d:
            continue
        valores += [d["medida"], d["li"], d["ls"]]

    xmin = max(0, min(valores) - 5)
    xmax = min(100, max(valores) + 5)

    altura = max(2.0, 0.5 * n + 0.8)
    fig, ax = plt.subplots(figsize=(9.5, altura))

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0.3, n + 1.4)

    for d in dados:
        if "header" in d:
            continue
        y = d["_y"]
        xerr = [[d["medida"] - d["li"]], [d["ls"] - d["medida"]]]
        ax.errorbar(
            d["medida"],
            y,
            xerr=xerr,
            fmt="s",
            ms=8,
            color=COR,
            ecolor=COR,
            elinewidth=1.5,
            capsize=3,
            zorder=3,
        )

    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.set_yticks([])
    ticks = ticks_bonitos(xmin, xmax)
    ax.set_xticks(ticks)
    ax.set_xticklabels([fmt(t) for t in ticks])
    ax.tick_params(axis="x", length=4)
    ax.set_xlabel(ROTULO_MEDIDA)

    tr = mtransforms.blended_transform_factory(ax.transAxes, ax.transData)
    x_rotulo, x_medida, x_p = -0.32, 1.06, 1.62

    y_cab = n + 0.9
    ax.text(
        x_rotulo,
        y_cab,
        "Variável",
        transform=tr,
        ha="left",
        va="center",
        fontweight="bold",
        clip_on=False,
    )
    ax.text(
        x_medida,
        y_cab,
        ROTULO_MEDIDA + " (IC 95%)",
        transform=tr,
        ha="left",
        va="center",
        fontweight="bold",
        clip_on=False,
    )
    ax.text(
        x_p,
        y_cab,
        "p-valor",
        transform=tr,
        ha="left",
        va="center",
        fontweight="bold",
        clip_on=False,
    )

    for d in dados:
        y = d["_y"]
        if "header" in d:
            ax.text(
                x_rotulo,
                y,
                d["header"],
                transform=tr,
                ha="left",
                va="center",
                fontweight="bold",
                clip_on=False,
            )
            continue
        ax.text(
            x_rotulo + 0.03,
            y,
            d["rotulo"],
            transform=tr,
            ha="left",
            va="center",
            clip_on=False,
        )
        ax.text(
            x_medida,
            y,
            texto_medida(d),
            transform=tr,
            ha="left",
            va="center",
            clip_on=False,
        )
        if d.get("p") is not None:
            ax.text(
                x_p,
                y,
                d["p"],
                transform=tr,
                ha="left",
                va="center",
                clip_on=False,
            )

    plt.subplots_adjust(left=0.24, right=0.62, top=0.88, bottom=0.15)
    fig.savefig(caminho_arquivo, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Salvo: {caminho_arquivo}")


if __name__ == "__main__":
    for nome_var, dados_var in VARIAVEIS.items():
        caminho = os.path.join(PASTA_SAIDA, f"forest_plot_{nome_var}.png")
        gerar_forest_plot(dados_var, caminho)
