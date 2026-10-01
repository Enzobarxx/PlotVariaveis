import os
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.ticker import FixedLocator, FixedFormatter, NullLocator

# ----------------------------------------------------------------------
# 1) CONFIGURAÇÕES GERAIS
# ----------------------------------------------------------------------
PASTA_SAIDA = r"C:\Users\enzol\Downloads\graficos_forest_tabela_1_ponderada"
NOME_ARQUIVO = "forest_plot_unico.png"
ROTULO_MEDIDA = "RP ajustada"
COR = "#1F7A54"  # verde do exemplo (troque por "#30207F" se quiser o roxo)

os.makedirs(PASTA_SAIDA, exist_ok=True)

# ----------------------------------------------------------------------
# 2) DADOS (Tabela 1) - ordem = ordem no gráfico
#    Cada variável: (título, [(rótulo, medida, li, ls, p), ...])
#    p = "Referência" marca a categoria de referência (losango vazio)
# ----------------------------------------------------------------------
VARIAVEIS = [
    ("Consumo de Carne", [
        ("< 5 vezes/semana", 1.00, 1.00, 1.00, "Referência"),
        ("≥ 5 vezes/semana", 1.04, 1.01, 1.07, "0,003"),
    ]),
    ("Consumo de Frango", [
        ("< 5 vezes/semana", 1.00, 1.00, 1.00, "Referência"),
        ("≥ 5 vezes/semana", 1.05, 1.02, 1.08, "0,002"),
    ]),
    ("Consumo Regular de Hortaliças e Verduras", [
        ("Sim", 1.00, 1.00, 1.00, "Referência"),
        ("Não", 1.01, 0.98, 1.03, "0,556"),
    ]),
    ("Consumo Regular de Frutas", [
        ("Sim", 1.00, 1.00, 1.00, "Referência"),
        ("Não", 0.98, 0.95, 1.00, "0,090"),
    ]),
    ("Consumo de Bebidas Adoçadas", [
        ("< 5 vezes/semana", 1.00, 1.00, 1.00, "Referência"),
        ("≥ 5 vezes/semana", 1.01, 0.96, 1.03, "0,886"),
    ]),
    ("Substitui Refeições por Lanches", [
        ("Não", 1.00, 1.00, 1.00, "Referência"),
        ("Sim", 1.04, 1.01, 1.07, "0,007"),
    ]),
    ("Tabagismo", [
        ("Não fumante", 1.00, 1.00, 1.00, "Referência"),
        ("Ex-fumante", 1.08, 1.05, 1.11, "< 0,001"),
        ("Fumante", 0.88, 0.84, 0.93, "< 0,001"),
    ]),
    ("Consumo Abusivo de Álcool", [
        ("Não", 1.00, 1.00, 1.00, "Referência"),
        ("Sim", 1.13, 1.10, 1.17, "< 0,001"),
    ]),
    ("Duração de Atividade Física", [
        ("≥ 60 min", 1.00, 1.00, 1.00, "Referência"),
        ("30–59 min", 0.99, 0.96, 1.01, "0,227"),
        ("< 30 min", 0.93, 0.89, 0.98, "0,009"),
    ]),
    ("Autoavaliação do Estado de Saúde", [
        ("Positiva", 1.00, 1.00, 1.00, "Referência"),
        ("Negativa", 1.27, 1.20, 1.35, "< 0,001"),
    ]),
]

# ----------------------------------------------------------------------
# 3) FUNÇÕES AUXILIARES
# ----------------------------------------------------------------------


def fmt(x):
    """1 casa decimal com vírgula (pt-BR)."""
    return f"{x:.1f}".replace(".", ",")


def fmt2(x):
    """2 casas decimais com vírgula (pt-BR)."""
    return f"{x:.2f}".replace(".", ",")


def texto_medida(medida, li, ls):
    return f"{fmt2(medida)} ({fmt2(li)} – {fmt2(ls)})"


# ----------------------------------------------------------------------
# 4) MONTA AS LINHAS (cabeçalhos + categorias) NUM ÚNICO GRÁFICO
# ----------------------------------------------------------------------
linhas = []
for titulo, categorias in VARIAVEIS:
    linhas.append({"tipo": "header", "texto": titulo})
    for rotulo, medida, li, ls, p in categorias:
        linhas.append({
            "tipo": "cat",
            "rotulo": rotulo,
            "medida": medida,
            "li": li,
            "ls": ls,
            "p": p,
            "ref": (p == "Referência"),
        })

n = len(linhas)
for i, l in enumerate(linhas):
    l["y"] = n - i

# Limites do eixo X (escala log)
todos = [l[k] for l in linhas if l["tipo"] == "cat" for k in ("li", "ls")]
xmin = min(todos) * 0.95
xmax = max(todos) * 1.05

# ----------------------------------------------------------------------
# 5) DESENHO
# ----------------------------------------------------------------------
altura = 0.34 * n + 1.8
fig, ax = plt.subplots(figsize=(10, altura))

ax.set_xscale("log")
ax.set_xlim(xmin, xmax)
ax.set_ylim(0.3, n + 1.4)

# Linha de referência em RP = 1
ax.axvline(x=1.0, color="gray", linestyle="--", linewidth=1, zorder=1)

# Pontos e intervalos
for l in linhas:
    if l["tipo"] != "cat":
        continue
    y = l["y"]
    if l["ref"]:
        ax.plot(1.0, y, marker="D", ms=8, mfc="white", mec=COR,
                mew=1.6, zorder=3)
    else:
        xerr = [[l["medida"] - l["li"]], [l["ls"] - l["medida"]]]
        ax.errorbar(l["medida"], y, xerr=xerr, fmt="s", ms=8,
                    color=COR, ecolor=COR, elinewidth=1.5,
                    capsize=3, zorder=3)

# Estilo dos eixos
for lado in ("top", "right", "left"):
    ax.spines[lado].set_visible(False)
ax.set_yticks([])

# Ticks do eixo X em notação decimal (sem 10^x)
candidatos = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5]
ticks = [t for t in candidatos if xmin <= t <= xmax]
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(FixedFormatter([fmt(t) for t in ticks]))
ax.xaxis.set_minor_locator(NullLocator())
ax.tick_params(axis="x", length=4)
ax.set_xlabel(f"{ROTULO_MEDIDA} (IC 95%)")

# Colunas de texto (x em coordenadas do eixo, y em dados)
tr = mtransforms.blended_transform_factory(ax.transAxes, ax.transData)
x_rotulo, x_medida, x_p = -0.55, 1.06, 1.62

y_cab = n + 0.9
for x, txt in ((x_rotulo, "Variável"),
               (x_medida, f"{ROTULO_MEDIDA} (IC 95%)"),
               (x_p, "p-valor")):
    ax.text(x, y_cab, txt, transform=tr, ha="left", va="center",
            fontweight="bold", clip_on=False)

for l in linhas:
    y = l["y"]
    if l["tipo"] == "header":
        ax.text(x_rotulo, y, l["texto"], transform=tr, ha="left",
                va="center", fontweight="bold", clip_on=False)
        continue

    ax.text(x_rotulo + 0.03, y, l["rotulo"], transform=tr, ha="left",
            va="center", clip_on=False)

    if l["ref"]:
        ax.text(x_medida, y, "1,00", transform=tr, ha="left",
                va="center", style="italic", color="dimgray",
                clip_on=False)
        ax.text(x_p, y, "—", transform=tr, ha="left", va="center",
                clip_on=False)
    else:
        ax.text(x_medida, y, texto_medida(l["medida"], l["li"], l["ls"]),
                transform=tr, ha="left", va="center", clip_on=False)
        ax.text(x_p, y, l["p"], transform=tr, ha="left", va="center",
                clip_on=False)

plt.subplots_adjust(left=0.30, right=0.62, top=0.97, bottom=0.06)

caminho = os.path.join(PASTA_SAIDA, NOME_ARQUIVO)
fig.savefig(caminho, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Salvo: {caminho}")
