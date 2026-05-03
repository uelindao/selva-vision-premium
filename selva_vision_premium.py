import streamlit as st
from datetime import datetime
from typing import List, Dict, Any
import html 

# ── configuração ──────────────────────────────────────────────────────────────
MAX_EXTRA_FURNITURE = 5

st.set_page_config(page_title="selva vision premium", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&family=Inter:wght@300;400;500&display=swap');
*,*::before,*::after{box-sizing:border-box;}
html,body,.stApp{background:#161615!important;color:#EAE8E3!important;font-family:'Inter',sans-serif!important;}
.stApp::before{display:none!important;}
.arch-header{text-align:center;padding:2.5rem 1rem 1.5rem;}
.arch-header h1{font-family:'Montserrat',sans-serif;font-size:3rem;font-weight:500;letter-spacing:-0.05em;color:#EAE8E3!important;line-height:1.1;margin-bottom:0.4rem;text-transform:lowercase;}
.arch-header p{color:#8C8881;font-size:0.9rem;font-family:'Inter',sans-serif;letter-spacing:0.02em;text-transform:lowercase;}
.arch-badge{display:inline-block;background:#1C1B1A;border:1px solid #213326;color:#8C8881;font-family:'Inter',sans-serif;font-size:0.7rem;letter-spacing:0.1em;padding:4px 14px;margin-bottom:1.2rem;text-transform:lowercase;}
.layer-label{font-family:'Montserrat',sans-serif!important;font-size:0.75rem;letter-spacing:0.1em;text-transform:lowercase;color:#8C8881!important;margin:1.4rem 0 0.8rem;display:flex;align-items:center;gap:8px;}
.layer-num{background:#1C1B1A!important;border:1px solid #213326!important;color:#EAE8E3!important;width:22px;height:22px;display:inline-flex;align-items:center;justify-content:center;font-size:0.65rem;flex-shrink:0;}
.furn-label{font-family:'Montserrat',sans-serif!important;font-size:0.7rem;letter-spacing:0.1em;text-transform:lowercase;color:#8C8881!important;margin:1rem 0 0.6rem;}
.prompt-panel{background:#1C1B1A!important;padding:1.4rem;position:sticky;top:1rem;}
.prompt-live-label{font-family:'Inter',sans-serif!important;font-size:0.7rem;letter-spacing:0.1em;text-transform:lowercase;color:#8C8881!important;display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;}
.meta-count{font-family:'Inter',sans-serif!important;font-size:0.65rem;color:#8C8881!important;margin:3px 0 10px;text-transform:lowercase;}
.section-sep{border:none!important;border-top:1px solid rgba(255,255,255,0.05)!important;margin:1rem 0;}
.hist-prompt{font-family:'Inter',sans-serif!important;font-size:0.75rem;color:#EAE8E3!important;line-height:1.7;background:#1C1B1A!important;padding:0.8rem;margin:0.5rem 0;white-space:pre-wrap;word-break:break-word;}
.stSelectbox>label,.stTextInput>label,.stTextArea>label,.stMultiSelect>label{font-family:'Inter',sans-serif!important;font-size:0.75rem!important;letter-spacing:0.02em!important;color:#8C8881!important;text-transform:lowercase!important;}
.stSelectbox>div>div,.stTextInput>div>div>input,.stTextArea>div>div>textarea{background:#121211!important;border:1px solid #2A2928!important;border-radius:0px!important;color:#EAE8E3!important;font-family:'Inter',sans-serif!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus,.stSelectbox>div[aria-expanded="true"]{outline:none!important;border:1px solid #C49A6C!important;box-shadow:none!important;}
.stButton>button{background:#213326!important;color:#EAE8E3!important;border:none!important;border-radius:0px!important;font-family:'Inter',sans-serif!important;font-weight:400!important;font-size:0.85rem!important;text-transform:lowercase!important;transition:all 0.2s ease-in-out!important;}
.stButton>button:hover{background:#1A291E!important;}
.stTabs [data-baseweb="tab-list"]{background:none!important;padding:0!important;border:none!important;margin-bottom:1rem;gap:1.5rem;}
.stTabs [data-baseweb="tab"]{font-family:'Inter',sans-serif!important;font-size:0.8rem!important;letter-spacing:0.05em!important;color:#8C8881!important;background:none!important;padding-bottom:0.5rem;text-transform:lowercase!important;}
.stTabs [aria-selected="true"]{color:#EAE8E3!important;border-bottom:1px solid #C49A6C!important;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding-top:0!important;max-width:1400px!important;}
[data-testid="stCodeBlock"], 
[data-testid="stCodeBlock"] > div, 
[data-testid="stCodeBlock"] pre, 
[data-testid="stCodeBlock"] code {white-space:pre-wrap!important;word-break:break-word!important;overflow-x:hidden!important;}
[data-testid="stCodeBlock"]{background:#121211!important;border:1px solid #2A2928!important;border-radius:0px!important;padding:1rem!important;}
[data-testid="stCodeBlock"] code{color:#EAE8E3!important;font-family:'Inter',sans-serif!important;font-size:0.85rem!important;background:transparent!important;}
.footer-container{display:flex;justify-content:space-between;margin-top:5rem;padding-top:3rem;border-top:1px solid #2A2928;color:#8C8881;font-family:'Inter',sans-serif;font-size:0.85rem;text-transform:lowercase;}
.footer-col{display:flex;flex-direction:column;gap:2rem;}
.footer-col-right{text-align:right;}
.footer-title{font-family:'Montserrat',sans-serif;font-size:1.1rem;color:#EAE8E3;margin-bottom:0.8rem;font-weight:400;letter-spacing:0.15em;text-transform:lowercase;}
.footer-text{margin:0.3rem 0;line-height:1.5;}
.footer-socials{display:flex;gap:1.2rem;font-size:1.5rem;margin-top:0.5rem;}
.footer-col-right .footer-socials{justify-content:flex-end;}
.footer-socials a{color:#EAE8E3;transition:color 0.2s ease;text-decoration:none;}
.footer-socials a:hover{color:#C49A6C;}
.footer-copy{text-align:right;margin-top:3rem;margin-bottom:2rem;font-size:0.75rem;color:#8C8881;text-transform:lowercase;}
@media(max-width:768px){.footer-container{flex-direction:column;gap:2.5rem;}.footer-col-right{text-align:left;}.footer-col-right .footer-socials{justify-content:flex-start;}.footer-copy{text-align:center;}}
</style>

<div class="arch-header">
    <span class="arch-badge">v1.2.0 · premium studio</span>
    <h1>selva vision</h1>
    <p>engenharia de prompts para visualização arquitetônica de alto padrão</p>
</div>
""", unsafe_allow_html=True)

# ── dicionários de dados ──────────────────────────────────────────────────────
ROOMS = {
    "quarto suíte": {
        "en": "bedroom suite",
        "furniture": {
            "cama": {"label": "cama (cabeceira e base)", "options": ["base estofada em tecido bouclé","cabeceira em couro caramelo","cabeceira em veludo grafite","base em madeira natural carvalho","cabeceira em lâmina de nogueira","base baixa estilo plataforma","outro"],
                "en_map": {"base estofada em tecido bouclé":"upholstered platform bed in bouclé fabric","cabeceira em couro caramelo":"caramel leather headboard with low wooden base","cabeceira em veludo grafite":"graphite velvet headboard, contemporary frame","base em madeira natural carvalho":"natural oak wood bed frame with clean lines","cabeceira em lâmina de nogueira":"walnut veneer headboard, integrated bedside panels","base baixa estilo plataforma":"low-profile platform bed, minimalist silhouette"}},
            "roupa_cama": {"label": "roupa de cama", "options": ["linho natural amassado","lençóis de algodão percal branco","manta de lã cinza trama grossa","conjunto veludo grafite","mix linho e algodão off-white","outro"],
                "en_map": {"linho natural amassado":"crushed natural linen bedding in warm ivory tones","lençóis de algodão percal branco":"crisp white percale cotton sheets","manta de lã cinza trama grossa":"thick weave grey wool throw casually draped","conjunto veludo grafite":"deep graphite velvet duvet with contrasting linen cushions","mix linho e algodão off-white":"mixed linen and cotton off-white layered bedding"}},
            "armario": {"label": "armário / roupeiro", "options": ["mdf lacca fosco acetinado","mdf bp freijó sincronizado","mdf lacca alto brilho","lâmina de madeira natural carvalho","lâmina de madeira nogueira","ripas em madeira com molduras","outro"],
                "en_map": {"mdf lacca fosco acetinado":"MDF matte lacquered wardrobe, floor-to-ceiling with slim push-to-open doors","mdf bp freijó sincronizado":"Freijó-pattern melamine wardrobe, synchronized wood grain","mdf lacca alto brilho":"high-gloss lacquered wardrobe, mirror-like finish","lâmina de madeira natural carvalho":"natural oak veneer wardrobe, matte oil finish","lâmina de madeira nogueira":"walnut veneer wardrobe, dark warm grain, integrated lighting","ripas em madeira com molduras":"wood slat wardrobe doors with geometric frame detail"}},
            "mesa_cabeceira": {"label": "mesa de cabeceira", "options": ["não incluir","suspenso em mdf com prateleira aberta","em madeira maciça carvalho","mármore calacatta com estrutura metálica","acrílico translúcido","nicho embutido na parede","outro"],
                "en_map": {"não incluir":"","suspenso em mdf com prateleira aberta":"wall-mounted MDF floating bedside table with open shelf","em madeira maciça carvalho":"solid oak bedside table with single drawer","mármore calacatta com estrutura metálica":"Calacatta marble top bedside table on slim brass metal legs","acrílico translúcido":"translucent acrylic bedside table","nicho embutido na parede":"built-in wall niche bedside with hidden LED lighting"}},
            "penteadeira": {"label": "penteadeira (opcional)", "options": ["não incluir","com espelho oval e base em madeira","embutida no armário com iluminação","mesa em mdf lacca com tampo em mármore","bancada com espelho de parede inteiro","outro"],
                "en_map": {"não incluir":"","com espelho oval e base em madeira":"wooden vanity table with oval standing mirror","embutida no armário com iluminação":"integrated vanity station inside wardrobe with Hollywood lighting","mesa em mdf lacca com tampo em mármore":"lacquered MDF vanity with marble top and wall mirror","bancada com espelho de parede inteiro":"full-width vanity countertop with floor-to-ceiling mirror"}},
        }
    },
    "sala de estar": {
        "en": "living room",
        "furniture": {
            "sofa": {"label": "sofá", "options": ["sofá curvo em veludo de algodão grafite","sofá modular em linho off-white","sofá retrátil em couro caramelo","sofá chesterfield em veludo verde-musgo","sofá de 3 lugares em tecido bouclé creme","outro"],
                "en_map": {"sofá curvo em veludo de algodão grafite":"curved sofa in graphite cotton velvet, sculptural silhouette","sofá modular em linho off-white":"modular sectional sofa in off-white linen, oversized cushions","sofá retrátil em couro caramelo":"reclining sofa in caramel genuine leather, wood legs","sofá chesterfield em veludo verde-musgo":"chesterfield sofa in moss green velvet, button tufted","sofá de 3 lugares em tecido bouclé creme":"3-seat sofa in cream bouclé wool, low-profile frame"}},
            "mesa_centro": {"label": "mesa de centro", "options": ["mármore calacatta em base metálica dourada","vidro fumê com estrutura em aço preto","madeira maciça carvalho forma orgânica","concreto aparente circular","tampo de mármore em base de madeira","outro"],
                "en_map": {"mármore calacatta em base metálica dourada":"Calacatta marble top coffee table on brushed gold metal base","vidro fumê com estrutura em aço preto":"smoked glass coffee table with matte black steel frame","madeira maciça carvalho forma orgânica":"solid oak coffee table with organic shaped top","concreto aparente circular":"circular raw concrete coffee table","tampo de mármore em base de madeira":"marble slab top on sculptural wooden base"}},
            "mesa_lateral": {"label": "mesa lateral (opcional)", "options": ["não incluir","mesa lateral em mármore com base metálica","mesa lateral em madeira redonda","mesa lateral em acrílico transparente","mesa lateral industrial em ferro e madeira","mesa lateral em rattan natural","outro"],
                "en_map": {"não incluir":"","mesa lateral em mármore com base metálica":"marble side table on slim brass tripod legs","mesa lateral em madeira redonda":"round solid wood side table, natural finish","mesa lateral em acrílico transparente":"transparent acrylic ghost side table","mesa lateral industrial em ferro e madeira":"industrial iron and wood side table","mesa lateral em rattan natural":"natural rattan woven side table"}},
            "poltrona": {"label": "poltrona / cadeira de apoio", "options": ["não incluir","poltrona egg em couro cognac","poltrona barcelona em couro preto","cadeira de balanço em madeira e tecido","poltrona bouclé com pés em latão","poltrona giratória em veludo azul-petróleo","outro"],
                "en_map": {"não incluir":"","poltrona egg em couro cognac":"egg-shaped lounge chair in cognac leather, swivel base","poltrona barcelona em couro preto":"Barcelona-style chair in black leather with chrome cross frame","cadeira de balanço em madeira e tecido":"wooden rocking chair with upholstered seat","poltrona bouclé com pés em latão":"bouclé armchair with brushed brass legs","poltrona giratória em veludo azul-petróleo":"swivel armchair in petrol blue velvet, walnut base"}},
            "painel_tv": {"label": "painel tv / rack (opcional)", "options": ["não incluir","painel de ripas em madeira com nicho suspenso","painel em mdf lacca fosco com iluminação embutida","rack suspenso em madeira com painel de cimento queimado","prateleiras abertas em madeira e metal","outro"],
                "en_map": {"não incluir":"","painel de ripas em madeira com nicho suspenso":"wall-mounted wood slat TV panel with floating shelves and integrated LED","painel em mdf lacca fosco com iluminação embutida":"matte lacquered MDF TV wall unit with hidden LED strip lighting","rack suspenso em madeira com painel de cimento queimado":"floating wood rack with burnished cement wall panel backdrop","prateleiras abertas em madeira e metal":"open wood and metal shelving unit with asymmetric layout"}},
        }
    },
    "cozinha gourmet": {
        "en": "gourmet kitchen",
        "furniture": {
            "armarios_coz": {"label": "armários / marcenaria", "options": ["mdf lacca fosco acetinado","mdf lacca alto brilho","mdf bp freijó sincronizado","mdf bp padrão amadeirado escuro","lâmina de madeira natural carvalho","bicolor: superior lacca + inferior madeira","outro"],
                "en_map": {"mdf lacca fosco acetinado":"satin matte lacquered MDF kitchen cabinets","mdf lacca alto brilho":"high-gloss lacquered kitchen cabinets","mdf bp freijó sincronizado":"Freijó synchronized melamine cabinets","mdf bp padrão amadeirado escuro":"dark wood pattern melamine cabinets","lâmina de madeira natural carvalho":"natural European oak veneer kitchen cabinets","bicolor: superior lacca + inferior madeira":"two-tone kitchen: upper cabinets matte lacquer, lower natural wood veneer"}},
            "bancada_coz": {"label": "bancada / tampo", "options": ["mdf carvalho","quartzito polido","mármore calacatta polido","porcelanato imitação mármore","concreto aparente moldado in loco","aço inoxidável escovado","pedra natural honed matte","outro"],
                "en_map": {"mdf carvalho":"natural oak MDF countertop with seamless edge","quartzito polido":"polished quartzite countertop with dramatic natural veining","mármore calacatta polido":"Calacatta marble countertop, continuous grey veining, high polish","porcelanato imitação mármore":"large-format marble-look porcelain countertop","concreto aparente moldado in loco":"cast-in-place raw concrete countertop with natural imperfections","aço inoxidável escovado":"brushed stainless steel countertop with subtle use marks","pedra natural honed matte":"honed natural stone countertop, tactile matte surface"}},
            "ilha": {"label": "ilha central (opcional)", "options": ["não incluir","ilha com tampo em mármore e estrutura em madeira","ilha em mdf lacca com tampo em quartzito","ilha industrial com tampo em aço","ilha com tampo oversize e banquetas","outro"],
                "en_map": {"não incluir":"","ilha com tampo em mármore e estrutura em madeira":"kitchen island with marble waterfall top and natural wood base","ilha em mdf lacca com tampo em quartzito":"lacquered MDF island base with thick quartzite top and seating overhang","ilha industrial com tampo em aço":"industrial steel-top kitchen island with open shelving","ilha com tampo oversize e banquetas":"oversized island countertop with integrated breakfast bar and tall stools"}},
        }
    },
    "banheiro": {
        "en": "bathroom",
        "furniture": {
            "cuba": {"label": "cuba / lavatório", "options": ["bica docol mix & match","cuba de apoio em cerâmica branca","cuba esculpida em mármore calacatta","cuba suspensa em corian branco","cuba retangular negra fosca","lavatório integrado ao tampo","cuba vessel de vidro translúcido","outro"],
                "en_map": {"bica docol mix & match":"Docol Mix and Match series minimalist wall-mounted spout (not a standard faucet)","cuba de apoio em cerâmica branca":"white ceramic vessel sink","cuba esculpida em mármore calacatta":"carved Calacatta marble monolithic sink","cuba suspensa em corian branco":"white corian undermount sink","cuba retangular negra fosca":"matte black rectangular undermount basin","lavatório integrado ao tampo":"integrated sink and countertop in continuous stone slab","cuba vessel de vidro translúcido":"transparent glass vessel sink"}},
            "tampo_ban": {"label": "tampo / bancada da pia", "options": ["mármore calacatta polido","quartzito polido","concreto aparente","porcelanato retificado","resina contínua","pedra natural honed","outro"],
                "en_map": {"mármore calacatta polido":"Calacatta marble vanity top with dramatic veining","quartzito polido":"polished quartzite vanity countertop","concreto aparente":"cast concrete vanity top, matte textured finish","porcelanato retificado":"rectified porcelain vanity top, large format","resina contínua":"seamless resin vanity surface","pedra natural honed":"honed natural stone vanity top"}},
            "box": {"label": "box / chuveiro", "options": ["box em vidro temperado sem moldura","chuveiro italiano a céu aberto","box em vidro fumê","box em alvenaria com nicho embutido","outro"],
                "en_map": {"box em vidro temperado sem moldura":"frameless tempered glass shower enclosure","chuveiro italiano a céu aberto":"open walk-in shower with ceiling rain head","box em vidro fumê":"smoked glass shower enclosure","box em alvenaria com nicho embutido":"tiled shower with built-in niche and bench"}},
        }
    },
    "fachada externa": {
        "en": "exterior facade",
        "furniture": {
            "rev_fachada": {"label": "revestimento principal", "options": ["light steel frame aparente","woodframe","tijolo ecológico solo-cimento","cimento queimado artesanal","concreto aparente com textura de fôrma","pedra natural (mármore, basalto, quartzito)","porcelanato de grandes dimensões","tijolo aparente","madeira termomodificada","cobre ou zinco natural oxidado","outro"],
                "en_map": {"light steel frame aparente":"exposed light steel frame structure, contemporary architectural style","woodframe":"timber woodframe construction, sustainable modern architecture","tijolo ecológico solo-cimento":"ecological soil-cement exposed brickwork, sustainable earthy facade","cimento queimado artesanal":"artisanal burnished cement facade, matte finish","concreto aparente com textura de fôrma":"board-formed exposed concrete facade","pedra natural (mármore, basalto, quartzito)":"natural stone cladding, monumental scale","porcelanato de grandes dimensões":"large-format architectural porcelain facade panels","tijolo aparente":"exposed brick facade, contemporary bond pattern","madeira termomodificada":"thermally modified wood cladding, silver grey patina","cobre ou zinco natural oxidado":"oxidized copper or zinc facade panels with natural patina"}},
            "esquadrias": {"label": "esquadrias / janelas", "options": ["alumínio preto maxim-ar de piso ao teto","madeira pintada de branco colonial","aço corten","alumínio natural anodizado","pvc branco com vidro duplo","parede inteira em vidro estrutural","outro"],
                "en_map": {"alumínio preto maxim-ar de piso ao teto":"floor-to-ceiling matte black aluminum framed windows and doors","madeira pintada de branco colonial":"painted white wood colonial window frames with shutters","aço corten":"weathering steel window frames with warm rust patina","alumínio natural anodizado":"natural anodized aluminum frames","pvc branco com vidro duplo":"white uPVC double-glazed windows","parede inteira em vidro estrutural":"full structural glass curtain wall facade"}},
        }
    }
}

STYLE_EN = {"moderno contemporâneo":"modern contemporary","minimalista":"minimalist","japandi":"japandi","brutalista":"brutalist","mid-century modern":"mid-century modern","escandinavo":"scandinavian","industrial":"industrial","warm minimalism":"warm minimalism","rústico":"rustic","outro":""}
VIEWPOINT_EN = {"nível do olho (eye-level)":"eye-level viewpoint","vista aérea (bird's eye)":"bird's eye view","perspectiva de canto":"corner perspective","vista frontal":"front view","outro":""}
FOCAL_EN = {"24mm (grande angular)":"24mm wide-angle lens","35mm (natural)":"35mm balanced lens","50mm (neutro)":"50mm neutral lens","85mm (detalhes)":"85mm compression lens","outro":""}
DOF_EN = {"rasa (foco no primeiro plano)":"shallow depth of field","média (equilíbrio)":"medium depth of field","profunda (tudo em foco)":"deep depth of field","outro":""}
LIGHTING_EN = {"golden hour (sol baixo)":("golden hour, low sun with long soft shadows","2700K"),"blue hour (crepúsculo)":("blue hour twilight, deep ambient","3200K"),"luz natural clara":("clear bright daylight","6500K"),"dia nublado (luz difusa)":("overcast diffused light, soft shadows","5500K"),"outro":("","")}
AMBIENT_EN = {"luz natural de janela":"wide window natural light","luz zenital (claraboia)":"skylight zenithal light","bounce light suave":"soft bounce fill light","outro":""}
TASK_EN = {"fita led sob armários 4000k":"4000K LED strips under cabinets","spots recuados (low-glare)":"low-glare recessed spotlights","outro":""}
ACCENT_EN = {"pendentes com vidro fosco":"frosted glass pendant lights","arandelas em latão":"brushed brass wall sconces","fita led rodapé 2700k":"2700K hidden LED baseboard strip","outro":""}
FLOOR_EN = {"mármore travertino levigado":"honed travertine marble floor","porcelanato acetinado":"satin-finish large-format porcelain floor","réguas de carvalho europeu":"wide-plank European oak floorboards","cimento queimado":"burnished cement floor","outro":""}
WALL_EN = {"textura de argila off-white":"natural clay-texture warm off-white walls","painéis de ripas em nogueira":"vertical walnut wood slat wall panels","concreto aparente":"board-formed exposed concrete walls","outro":""}
METALS_EN = {"alumínio preto escovado":"brushed matte black aluminum","latão escovado dourado":"brushed warm brass","aço inox escovado":"brushed stainless steel","cobre":"natural copper","outro":""}
CAMERA_EN = {"nenhum":"","sony a7iii":"shot on Sony A7III","hasselblad x2d":"shot on Hasselblad X2D","outro":""}
RESOLUTION_EN = {"4k nativo":"4K native resolution","hd":"HD resolution"}
RATIO_EN = {"16:9 (paisagem)":"16:9 aspect ratio","9:16 (vertical)":"9:16 aspect ratio","1:1 (quadrado)":"1:1 aspect ratio"}
THINKING_EN = {"máxima qualidade":"highly detailed, masterpiece","iteração rápida":"fast concept render"}

# ── ecossistema selva urbana ─────────────────────────────────────────────────
SUSTENTABILIDADE_EN = {"painéis solares integrados": "architecturally integrated solar panels with precise roof continuity", "telhado verde": "lush green roof system", "cisterna de captação": "architectural rainwater harvesting cistern", "brises ecológicos": "sustainable solar shading brises"}
BIOFILIA_EN = {"jardim de inverno": "indoor winter garden with dense tropical biophilia", "piscina natural": "natural pool with biological filtration and organic pebble borders", "horta integrada": "integrated organic herb garden", "vegetação pendente": "cascading biophilic elements from ceiling"}
AUTOMACAO_EN = {"painel inteligente minimalista": "minimalist smart home automation wall panels", "iluminação circadiana": "circadian rhythm smart lighting integration", "climatização invisível": "invisible linear slot diffusers for climate control"}


# ── histórico de sessão seguro (isolado por usuário) ──────────────────────────
def load_history() -> List[Dict[str, str]]:
    if "prompt_history" not in st.session_state:
        st.session_state.prompt_history = []
    return st.session_state.prompt_history

def save_history(entry: Dict[str, str]) -> None:
    if "prompt_history" not in st.session_state:
        st.session_state.prompt_history = []
    st.session_state.prompt_history.insert(0, entry)
    st.session_state.prompt_history = st.session_state.prompt_history[:100]

def clear_history() -> None:
    st.session_state.prompt_history = []

def init(k: str, v: Any) -> None:
    if k not in st.session_state:
        st.session_state[k] = v

init("extra_furn_count", 0)

# ── motor de prompt otimizado (fluido e natural) ─────────────────────────────
def build_prompt() -> str:
    room_key = st.session_state.get("w_room", list(ROOMS.keys())[0])
    
    if room_key == "outro":
        room_en = st.session_state.get("w_room_custom", "").strip() or "space"
    else:
        room_en = ROOMS.get(room_key, {}).get("en", "space")

    style_raw = st.session_state.get("w_style", "moderno contemporâneo")
    style_en = STYLE_EN.get(style_raw, style_raw) if style_raw != "outro" else st.session_state.get("w_style_custom", "").strip()

    # base e ponto de vista
    vp_raw = st.session_state.get("w_viewpoint", "nível do olho (eye-level)")
    vp_en = VIEWPOINT_EN.get(vp_raw, "") if vp_raw != "outro" else st.session_state.get("w_viewpoint_custom", "").strip()
    
    prompt = f"An architectural interior photography from a {vp_en} of a {room_en}, featuring {style_en} design."

    # contexto e localização
    ctx = []
    if loc := st.session_state.get("w_location", "").strip(): ctx.append(f"located in {loc}")
    topo_map = {"plana":"flat terrain","costeira":"coastal terrain","rural isolada":"isolated rural landscape"}
    if topo_en := topo_map.get(st.session_state.get("w_topo", ""), ""): ctx.append(f"on a {topo_en}")
    if veg := st.session_state.get("w_vegetation", "").strip(): ctx.append(f"surrounded by {veg} vegetation")
    if ctx: prompt += f" The space is {', '.join(ctx)}."
    
    if special := st.session_state.get("w_special", "").strip():
        prompt += f" Unique architectural features include {special}."

    # luz (essencial para fotorrealismo)
    light_raw = st.session_state.get("w_light", "luz natural clara")
    light_desc, kelvin = LIGHTING_EN.get(light_raw, ("clear bright daylight", ""))
    if light_raw == "outro": light_desc = st.session_state.get("w_light_custom", "").strip()
    if kc := st.session_state.get("w_kelvin_custom", "").strip(): kelvin = kc
    
    light_str = f"The atmosphere is defined by {light_desc}" + (f" at {kelvin}" if kelvin else "")
    
    extras_luz = [AMBIENT_EN.get(x, x) for x in st.session_state.get("w_ambient", []) if x != "outro"]
    if "outro" in st.session_state.get("w_ambient", []):
        custom_amb = st.session_state.get("w_ambient_custom", "").strip()
        if custom_amb: extras_luz.append(custom_amb)
        
    if extras_luz: light_str += f", enhanced by {', '.join(extras_luz)}"
    prompt += f" {light_str}."

    # materialidade
    floor_raw = st.session_state.get("w_floor", "")
    floor_en = FLOOR_EN.get(floor_raw, floor_raw) if floor_raw != "outro" else st.session_state.get("w_floor_custom", "").strip()
    wall_raw = st.session_state.get("w_walls", "")
    wall_en = WALL_EN.get(wall_raw, wall_raw) if wall_raw != "outro" else st.session_state.get("w_walls_custom", "").strip()
    
    if floor_en and wall_en:
        prompt += f" Materials highlight {wall_en} and a {floor_en}."
    elif floor_en or wall_en:
        prompt += f" The space features {floor_en or wall_en}."

    # metais
    metals_raw = st.session_state.get("w_metals", [])
    m_en = [METALS_EN.get(m, m) for m in metals_raw if m != "outro"]
    if m_en: prompt += f" Hardware and accent details are finished in {', '.join(m_en)}."

    # adição de sustentabilidade, biofilia e automação (selva dna)
    eco_raw = st.session_state.get("w_eco", [])
    eco_en = [SUSTENTABILIDADE_EN.get(e, e) for e in eco_raw]
    bio_raw = st.session_state.get("w_bio", [])
    bio_en = [BIOFILIA_EN.get(b, b) for b in bio_raw]
    auto_raw = st.session_state.get("w_auto", [])
    auto_en = [AUTOMACAO_EN.get(a, a) for a in auto_raw]
    
    selva_elements = eco_en + bio_en + auto_en
    if selva_elements:
        prompt += f" Integrating state-of-the-art systems and nature, the design includes {', '.join(selva_elements)}."

    # mobiliário
    fp = []
    if room_key != "outro":
        for fkey, fdata in ROOMS.get(room_key, {}).get("furniture", {}).items():
            val = st.session_state.get(f"w_furn_{fkey}", "")
            if val not in ("", "não incluir"):
                en_val = fdata.get("en_map", {}).get(val, val) if val != "outro" else st.session_state.get(f"w_furn_{fkey}_custom", "").strip()
                if en_val: fp.append(en_val)
            
    for i in range(st.session_state.get("extra_furn_count", 0)):
        if v := st.session_state.get(f"w_extra_furn_{i}", "").strip(): fp.append(v)
        
    if fp: prompt += f" It is beautifully furnished with {', '.join(fp)}."

    # detalhes humanos
    if human := st.session_state.get("w_human", "").strip():
        prompt += f" Lived-in details like {human} add a sense of realism."

    # fotografia e câmera
    focal_raw = st.session_state.get("w_focal", "")
    focal = FOCAL_EN.get(focal_raw, "") if focal_raw != "outro" else st.session_state.get("w_focal_custom", "").strip()
    
    dof_raw = st.session_state.get("w_dof", "")
    dof = DOF_EN.get(dof_raw, "") if dof_raw != "outro" else st.session_state.get("w_dof_custom", "").strip()
    
    cam = CAMERA_EN.get(st.session_state.get("w_camera", ""), "")
    res = RESOLUTION_EN.get(st.session_state.get("w_resolution", "4k nativo"), "4K native resolution")
    ratio = RATIO_EN.get(st.session_state.get("w_ratio", "16:9 (paisagem)"), "16:9 aspect ratio")
    think = THINKING_EN.get(st.session_state.get("w_thinking", "máxima qualidade"), "highly detailed")
    
    tech = [t for t in [focal, dof, cam] if t]
    if tech: prompt += f" Captured using {', '.join(tech)}."
    prompt += f" {think}, {res}, {ratio}, photorealistic architectural visualization, masterpiece."

    # trava de segurança e fidelidade técnica
    prompt += " CRITICAL INSTRUCTION: Strictly maintain the original architectural modeling and structural roof continuity. Do not alter or distort the base geometry. Do not add unrequested light fixtures or luminaires. Hardware must be exact as described."

    neg_base = "altered modeling, fake lighting, unrequested luminaires, structural changes, generic faucets, 3d look, plastic textures, distorted geometry"
    user_neg = st.session_state.get("w_negative", "").strip()
    prompt += f" Negative: {neg_base}" + (f", {user_neg}." if user_neg else ".")

    return " ".join(prompt.split())

# ── interface de usuário ──────────────────────────────────────────────────────

tab_builder, tab_history = st.tabs(["construtor de prompt", "histórico"])

with tab_builder:
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    col_form, col_prompt = st.columns([1.1, 0.9], gap="large")

    with col_form:
        st.markdown('<div class="layer-label"><span class="layer-num">1</span> sujeito do projeto</div>', unsafe_allow_html=True)
        room_opts = list(ROOMS.keys()) + ["outro"]
        init("w_room", room_opts[0])
        st.selectbox("tipo de ambiente", room_opts, key="w_room")
        selected_room = st.session_state["w_room"]
        
        if selected_room == "outro":
            init("w_room_custom", "")
            st.text_input("descrever ambiente", key="w_room_custom", placeholder="ex: adega subterrânea, hall de entrada...")

        style_opts = list(STYLE_EN.keys())
        init("w_style", style_opts[0])
        st.selectbox("estilo arquitetônico", style_opts, key="w_style")
        if st.session_state["w_style"] == "outro":
            init("w_style_custom", "")
            st.text_input("descrever estilo", key="w_style_custom", placeholder="ex: mediterrâneo...")

        init("w_special", "")
        st.text_input("características especiais (opcional)", key="w_special", placeholder="ex: pé direito duplo")

        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">2</span> ambiente e contexto</div>', unsafe_allow_html=True)
        init("w_location", "")
        st.text_input("localização geográfica (opcional)", key="w_location", placeholder="ex: são paulo")

        topo_opts = ["não se aplica (interior)","plana","costeira","rural isolada","outro"]
        init("w_topo", topo_opts[0])
        st.selectbox("topografia", topo_opts, key="w_topo")
        if st.session_state["w_topo"] == "outro":
            init("w_topo_custom", "")
            st.text_input("descrever topografia", key="w_topo_custom")

        init("w_vegetation", "")
        st.text_input("vegetação (opcional)", key="w_vegetation", placeholder="ex: pinus pinea, bambu")

        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">3</span> composição e câmera</div>', unsafe_allow_html=True)
        vp_opts = list(VIEWPOINT_EN.keys())
        init("w_viewpoint", vp_opts[0])
        st.selectbox("ponto de vista", vp_opts, key="w_viewpoint", help="define o ângulo da câmera. 'nível do olho' traz realismo imersivo, enquanto 'vista aérea' ajuda a entender o layout geral do espaço.")
        if st.session_state["w_viewpoint"] == "outro":
            init("w_viewpoint_custom", "")
            st.text_input("descrever: ponto de vista", key="w_viewpoint_custom")

        focal_opts = list(FOCAL_EN.keys())
        init("w_focal", focal_opts[1])
        st.selectbox("distância focal", focal_opts, key="w_focal", help="simula a lente da câmera. 24mm (angular) mostra mais do ambiente mas pode distorcer as bordas. 35mm ou 50mm são ideais para manter as proporções reais da arquitetura.")
        if st.session_state["w_focal"] == "outro":
            init("w_focal_custom", "")
            st.text_input("descrever: distância focal", key="w_focal_custom")

        dof_opts = list(DOF_EN.keys())
        init("w_dof", dof_opts[1])
        st.selectbox("profundidade de campo", dof_opts, key="w_dof", help="controla o desfoque de fundo. 'profunda' mantém tudo nítido (ideal para arquitetura geral), enquanto 'rasa' foca em um detalhe e desfoca o resto.")
        if st.session_state["w_dof"] == "outro":
            init("w_dof_custom", "")
            st.text_input("descrever: profundidade de campo", key="w_dof_custom")
        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">4</span> arquitetura da luz</div>', unsafe_allow_html=True)
        light_opts = list(LIGHTING_EN.keys())
        init("w_light", light_opts[2])
        st.selectbox("luz principal", light_opts, key="w_light", help="define o clima do render. 'dia nublado' cria luz difusa perfeita para materiais e texturas, enquanto 'golden hour' traz sombras longas e aconchego.")
        if st.session_state["w_light"] == "outro":
            init("w_light_custom", "")
            st.text_input("descrever: luz principal", key="w_light_custom")

        init("w_kelvin_custom", "")
        st.text_input("temperatura de cor (opcional)", key="w_kelvin_custom", placeholder="ex: 3000k", help="medida em kelvin. valores baixos (ex: 2700k) deixam a luz mais quente e amarelada. valores altos (ex: 6500k) deixam a cena mais fria e azulada.")

        ambient_opts = list(AMBIENT_EN.keys())
        init("w_ambient", [])
        st.multiselect("iluminação ambiente", ambient_opts, key="w_ambient", help="luzes secundárias que preenchem as sombras e dão volume e profundidade para a imagem gerada.")
        if "outro" in st.session_state["w_ambient"]:
            init("w_ambient_custom", "")
            st.text_input("descrever: iluminação ambiente", key="w_ambient_custom")
        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">5</span> materialidade e mobiliário</div>', unsafe_allow_html=True)
        floor_opts = [""] + list(FLOOR_EN.keys())
        init("w_floor", "")
        st.selectbox("piso principal", floor_opts, key="w_floor")
        if st.session_state["w_floor"] == "outro":
            init("w_floor_custom", "")
            st.text_input("descrever: piso principal", key="w_floor_custom")

        wall_opts = [""] + list(WALL_EN.keys())
        init("w_walls", "")
        st.selectbox("revestimento de parede", wall_opts, key="w_walls")
        if st.session_state["w_walls"] == "outro":
            init("w_walls_custom", "")
            st.text_input("descrever: revestimento de parede", key="w_walls_custom")

        st.markdown(f'<div class="furn-label">mobiliário — {selected_room}</div>', unsafe_allow_html=True)
        
        # carrega móveis padrão apenas se NÃO for "outro"
        if selected_room != "outro":
            room_data = ROOMS.get(selected_room, {})
            if furniture_data := room_data.get("furniture", {}):
                for fkey, fdata in furniture_data.items():
                    furn_opts = ["não incluir"] + fdata["options"]
                    init(f"w_furn_{fkey}", "não incluir")
                    st.selectbox(fdata["label"], furn_opts, key=f"w_furn_{fkey}")
                    if st.session_state[f"w_furn_{fkey}"] == "outro":
                        init(f"w_furn_{fkey}_custom", "")
                        st.text_input(f"descrever: {fdata['label']}", key=f"w_furn_{fkey}_custom")

        # móveis customizados carregam sempre (independente do ambiente)
        count = st.session_state.get("extra_furn_count", 0)
        for i in range(count):
            c1, c2 = st.columns([5, 1])
            with c1:
                init(f"w_extra_furn_{i}", "")
                st.text_input(f"item adicional {i+1}", key=f"w_extra_furn_{i}", placeholder="ex: tapete persa")
            with c2:
                st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)
                if st.button("✕", key=f"rm_{i}"):
                    for j in range(i, count - 1): st.session_state[f"w_extra_furn_{j}"] = st.session_state.get(f"w_extra_furn_{j+1}", "")
                    st.session_state[f"w_extra_furn_{count-1}"] = ""
                    st.session_state["extra_furn_count"] = max(0, count - 1); st.rerun()

        if count < MAX_EXTRA_FURNITURE:
            if st.button(f"＋ adicionar item ({count}/{MAX_EXTRA_FURNITURE})"):
                st.session_state["extra_furn_count"] = count + 1; st.rerun()

        init("w_human", "")
        st.text_input("elementos de humanização (opcional)", key="w_human", placeholder="ex: livros abertos")

        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">6</span> tecnologia, sustentabilidade e biofilia</div>', unsafe_allow_html=True)
        init("w_eco", [])
        st.multiselect("soluções de sustentabilidade", list(SUSTENTABILIDADE_EN.keys()), key="w_eco")
        
        init("w_bio", [])
        st.multiselect("design biofílico interno", list(BIOFILIA_EN.keys()), key="w_bio")
        
        init("w_auto", [])
        st.multiselect("sistemas de automação", list(AUTOMACAO_EN.keys()), key="w_auto")
        st.markdown("<hr class='section-sep'>", unsafe_allow_html=True)

        st.markdown('<div class="layer-label"><span class="layer-num">7</span> metadados técnicos</div>', unsafe_allow_html=True)
        cam_opts = list(CAMERA_EN.keys())
        init("w_camera", "nenhum")
        st.selectbox("equipamento fotográfico", cam_opts, key="w_camera", help="força a ia a simular a granulação, a paleta de cores e o nível de textura dos sensores de câmeras profissionais reais de alto padrão.")

        col_r, col_ra = st.columns(2)
        with col_r:
            init("w_resolution", "4k nativo")
            st.selectbox("resolução", list(RESOLUTION_EN.keys()), key="w_resolution", help="adiciona metadados de fidelidade para garantir bordas nítidas na arquitetura e ausência de ruídos na imagem.")
        with col_ra:
            init("w_ratio", "16:9 (paisagem)")
            st.selectbox("proporção", list(RATIO_EN.keys()), key="w_ratio", help="formato de corte do render. 16:9 é excelente para visualização em telas e apresentações, enquanto 9:16 é o formato vertical ideal para reels e stories do instagram.")

        init("w_thinking", "máxima qualidade")
        st.selectbox("modo de processamento", list(THINKING_EN.keys()), key="w_thinking", help="tags finais de instrução que orientam o modelo gerador sobre a complexidade e o grau de polimento artístico do resultado final.")

        init("w_negative", "")
        st.text_area("prompt negativo adicional", key="w_negative", height=70, placeholder="ex: distorção, pessoas", help="o que a ia deve PROIBIR. nossa programação base já bloqueia distorções estruturais e luzes falsas, mas você pode adicionar mais elementos indesejados aqui (ex: reflexos ruins, pessoas, plantas mortas).")

    with col_prompt:
        prompt = build_prompt()
        st.markdown('<div class="prompt-panel"><div class="prompt-live-label"><span>prompt em tempo real</span></div></div>', unsafe_allow_html=True)
        edited = st.text_area("prompt gerado (editável):", value=prompt, height=360)
        st.markdown(f'<div class="meta-count">{len(edited.split())} palavras · {len(edited)} caracteres</div>', unsafe_allow_html=True)

        st.markdown("<div style='font-family:\"Inter\",sans-serif; font-size:0.7rem; color:#8C8881; margin-top: 10px;'>cópia rápida:</div>", unsafe_allow_html=True)
        st.code(edited, language="text")

        st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        if st.button("salvar no histórico", use_container_width=True):
            save_history({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "ambiente": st.session_state.get("w_room", ""), "estilo": st.session_state.get("w_style", ""), "prompt": edited})
            st.success("salvo!")

with tab_history:
    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    history = load_history()
    if not history:
        st.markdown('<div style="text-align:center;padding:3rem;color:#8C8881;font-family:\'Inter\',sans-serif;font-size:0.8rem;">nenhum prompt salvo.</div>', unsafe_allow_html=True)
    else:
        c1, c2 = st.columns([3, 1])
        with c1: st.markdown(f'<div style="font-family:\'Inter\',sans-serif;font-size:0.75rem;color:#8C8881;padding:6px 0;">{len(history)} prompt(s) salvos</div>', unsafe_allow_html=True)
        with c2:
            if st.button("limpar histórico"): clear_history(); st.rerun()

        for i, entry in enumerate(history):
            prm = entry.get("prompt", "")
            prm_safe = html.escape(prm)
            with st.expander(f"{entry.get('timestamp','')} — {entry.get('ambiente','')} · {entry.get('estilo','')}", expanded=(i==0)):
                st.markdown(f'<div class="hist-prompt">{prm_safe}</div>', unsafe_allow_html=True)
                st.code(prm, language="text")

# ── rodapé fixo ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-container">
    <div class="footer-col">
        <div>
            <div class="footer-title">contato</div>
            <div class="footer-text">selvaurbanaprojetos@gmail.com</div>
            <div class="footer-text">55 51 99251-4815</div>
            <div class="footer-text">55 51 98088-6131</div>
        </div>
        <div>
            <div class="footer-title">redes sociais</div>
            <div class="footer-socials">
                <a href="https://wa.me/5551992514815" target="_blank" title="whatsapp"><i class="fab fa-whatsapp"></i></a>
                <a href="https://br.pinterest.com/selvaurbana_/" target="_blank" title="pinterest"><i class="fab fa-pinterest"></i></a>
                <a href="https://instagram.com/selva.urb" target="_blank" title="instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/selvaurbanaprojetos" target="_blank" title="facebook"><i class="fab fa-facebook"></i></a>
                <a href="https://linkedin.com/company/selvaurbanaprojetos" target="_blank" title="linkedin"><i class="fab fa-linkedin"></i></a>
            </div>
        </div>
    </div>
    <div class="footer-col footer-col-right">
        <div>
            <div class="footer-title">localização</div>
            <div class="footer-text">av. benjamin constant, 1194</div>
            <div class="footer-text">ed. diamond center, sala 702</div>
            <div class="footer-text">cep 95900-056, lajeado/rs</div>
        </div>
    </div>
</div>
<div class="footer-copy">© 2026 selva urbana ltda. todos os direitos reservados.</div>
""", unsafe_allow_html=True)