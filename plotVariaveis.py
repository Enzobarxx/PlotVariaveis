import os
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

# ----------------------------------------------------------------------
# 1) CONFIGURAÇÕES GERAIS
# ----------------------------------------------------------------------
PASTA_SAIDA = r"C:\Users\enzol\Downloads\graficos_forest_tabela_1_ponderada"
ROTULO_MEDIDA = "RP ajustada"
COR = "#30207F"

# Cria a pasta caso não exista
os.makedirs(PASTA_SAIDA, exist_ok=True)

# ----------------------------------------------------------------------
# 2) DADOS DAS VARIÁVEIS (Tabela 1)
# ----------------------------------------------------------------------
VARIAVEIS = {

    "01_consumo_carne": [
        {"header": "Consumo de Carne"},
        {
            "rotulo": "< 5 vezes/semana",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "≥ 5 vezes/semana",
            "medida": 1.04,
            "li": 1.01,
            "ls": 1.07,
            "p": "0,003",
        },
    ],

    "02_consumo_frango": [
        {"header": "Consumo de Frango"},
        {
            "rotulo": "< 5 vezes/semana",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "≥ 5 vezes/semana",
            "medida": 1.05,
            "li": 1.02,
            "ls": 1.08,
            "p": "0,002",
        },
    ],

    "03_hortalicas_verduras": [
        {"header": "Consumo Regular de Hortaliças e Verduras"},
        {
            "rotulo": "Sim",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Não",
            "medida": 1.01,
            "li": 0.98,
            "ls": 1.03,
            "p": "0,556",
        },
    ],

    "04_consumo_frutas": [
        {"header": "Consumo Regular de Frutas"},
        {
            "rotulo": "Sim",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Não",
            "medida": 0.98,
            "li": 0.95,
            "ls": 1.00,
            "p": "0,090",
        },
    ],

    "05_bebidas_adocadas": [
        {"header": "Consumo de Bebidas Adoçadas"},
        {
            "rotulo": "< 5 vezes/semana",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "≥ 5 vezes/semana",
            "medida": 1.01,
            "li": 0.96,
            "ls": 1.03,
            "p": "0,886",
        },
    ],

    "06_substitui_refeicoes": [
        {"header": "Substitui Refeições por Lanches"},
        {
            "rotulo": "Não",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Sim",
            "medida": 1.04,
            "li": 1.01,
            "ls": 1.07,
            "p": "0,007",
        },
    ],

    "07_tabagismo": [
        {"header": "Tabagismo"},
        {
            "rotulo": "Não fumante",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Ex-fumante",
            "medida": 1.08,
            "li": 1.05,
            "ls": 1.11,
            "p": "< 0,001",
        },
        {
            "rotulo": "Fumante",
            "medida": 0.88,
            "li": 0.84,
            "ls": 0.93,
            "p": "< 0,001",
        },
    ],

    "08_consumo_abusivo_alcool": [
        {"header": "Consumo Abusivo de Álcool"},
        {
            "rotulo": "Não",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Sim",
            "medida": 1.13,
            "li": 1.10,
            "ls": 1.17,
            "p": "< 0,001",
        },
    ],

    "09_duracao_atividade_fisica": [
        {"header": "Duração de Atividade Física"},
        {
            "rotulo": "< 30 min",
            "medida": 0.93,
            "li": 0.89,
            "ls": 0.98,
            "p": "0,009",
        },
        {
            "rotulo": "30–59 min",
            "medida": 0.99,
            "li": 0.96,
            "ls": 1.01,
            "p": "0,227",
        },
        {
            "rotulo": "≥ 60 min",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
    ],

    "10_autoavaliacao_saude": [
        {"header": "Autoavaliação do Estado de Saúde"},
        {
            "rotulo": "Positiva",
            "medida": 1.00,
            "li": 1.00,
            "ls": 1.00,
            "p": "Referência",
        },
        {
            "rotulo": "Negativa",
            "medida": 1.27,
            "li": 1.20,
            "ls": 1.35,
            "p": "< 0,001",
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

    ax.axvline(
    x=1.0,
    color="gray",
    linestyle="--",
    linewidth=1
)

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
