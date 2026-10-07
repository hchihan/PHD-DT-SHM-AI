"""Build the MDPI (Buildings) version of Paper 2: numbered citations in order of first appearance."""
import re, sys, pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE / "v3_source.md"
OUT = HERE.parent / "PAPER2_MANUSCRIPT_v3_Buildings.md"

REFS = {
 "parn2017": "Pärn, E.A.; Edwards, D.J.; Sing, M.C.P. The building information modelling trajectory in facilities management: A review. *Autom. Constr.* **2017**, *75*, 45–55. https://doi.org/10.1016/j.autcon.2016.12.003",
 "patacas2020": "Patacas, J.; Dawood, N.; Kassem, M. BIM for facilities management: A framework and a common data environment using open standards. *Autom. Constr.* **2020**, *120*, 103366. https://doi.org/10.1016/j.autcon.2020.103366",
 "bellon2025": "Bellon, F.G.; Martins, A.C.P.; de Carvalho, J.M.F.; de Souza, C.A.F.; Ribeiro, J.C.L.; César Júnior, K.M.L.; de Oliveira, D.S. IFC framework for inspection and maintenance representation in facility management. *Autom. Constr.* **2025**, *174*, 106157. https://doi.org/10.1016/j.autcon.2025.106157",
 "hagedorn2023": "Hagedorn, P.; Liu, L.; König, M.; Hajdin, R.; Blumenfeld, T.; Stöckner, M.; Billmaier, M.; Großauer, K.; Gavin, K. BIM-enabled infrastructure asset management using information containers and semantic web. *J. Comput. Civ. Eng.* **2023**, *37*, [article number]. https://doi.org/10.1061/(ASCE)CP.1943-5487.0001051",
 "kim2018": "Kim, K.; Kim, H.; Kim, W.; Kim, C.; Kim, J.; Yu, J. Integration of IFC objects and facility management work information using Semantic Web. *Autom. Constr.* **2018**, *87*, 173–187. https://doi.org/10.1016/j.autcon.2017.12.019",
 "marmo2020": "Marmo, R.; Polverino, F.; Nicolella, M.; Tibaut, A. Building performance and maintenance information model based on IFC schema. *Autom. Constr.* **2020**, *118*, 103275. https://doi.org/10.1016/j.autcon.2020.103275",
 "delgado2018": "Delgado, J.M.D.; et al. Structural performance monitoring using a dynamic data-driven BIM environment. *J. Comput. Civ. Eng.* **2018**, *32*, [article number]. https://doi.org/10.1061/(ASCE)CP.1943-5487.0000749 [complete author list]",
 "chatsuwan2025a": "Chatsuwan, M.; Ichinose, M.; Alkhalaf, H. Enhancing facility management with a BIM and IoT integration tool and framework in an open standard environment. *Buildings* **2025**, *15*, 1928. https://doi.org/10.3390/buildings15111928",
 "ramonell2023": "Ramonell, C.; Chacón, R.; Posada, H. Knowledge graph-based data integration system for digital twins of built assets. *Autom. Constr.* **2023**, *156*, 105109. https://doi.org/10.1016/j.autcon.2023.105109",
 "rogage2020": "Rogage, K.; et al. Data transfer between digital models of built assets and their operation & maintenance systems. *J. Inf. Technol. Constr.* **2020**, *25*, 469–481. https://doi.org/10.36680/j.itcon.2020.027 [complete author list]",
 "borkowski2026": "Borkowski, A.S.; Jarema, P.; Kładź, M.; Smoliar, A. Temporally qualified building elements: A DOLCE-based ontology for phase-dependent identity and change tracking in BIM models. *Technologies* **2026**, *14*, 413. https://doi.org/10.3390/technologies14070413",
 "fang2025": "Fang, Z.; Teng, X.; Shen, Z.; Yang, D.; Lin, X. Standardizing design-stage digital-twin assets in a smart home for building data management: Workflow design and validation based on IfcGUID compliance. *Buildings* **2025**, *15*, 4096. https://doi.org/10.3390/buildings15224096",
 "mariniello2025": "Mariniello, G.; Gragnaniello, C.; Asprone, D. Enhancing structural health monitoring data management and damage detection in digital twins with blockchain and smart contracts. *Autom. Constr.* **2025**, *180*, 106558. https://doi.org/10.1016/j.autcon.2025.106558",
 "garcia2026": "García, J.A.; Toledo, I.; Aragonés, L.; Bañón, L. A CDE-centered quality gate framework to operationalize ISO 19650 governance in hybrid railway depots. *Appl. Sci.* **2026**, *16*, 2562. https://doi.org/10.3390/app16052562",
 "kochovski2026": "Kochovski, P.; Fujs, D.; Vavpotič, D.; Chiachío, J.; Miri, P.; Stankovski, V. Leveraging IFC semantics and W3C decentralized identifiers for Digital Building Logbooks in construction and deep renovation. *Autom. Constr.* **2026**, *189*, 107065. https://doi.org/10.1016/j.autcon.2026.107065",
 "lorvao2024": "Lorvão Antunes, A.; Barateiro, J.; Marecos, V.; Petrović, J.; Cardoso, E. Ontology-based BIM-AMS integration in European highways. *Intell. Syst. Appl.* **2024**, *22*, 200366. https://doi.org/10.1016/j.iswa.2024.200366",
 "panah2021": "Shafie Panah, R.; Kioumarsi, M. Application of building information modelling (BIM) in the health monitoring and maintenance process: A systematic review. *Sensors* **2021**, *21*, 837. https://doi.org/10.3390/s21030837",
 "sadhu2023": "Sadhu, A.; Peplinski, J.E.; Mohammadkhorasani, A.; Moreu, F. A review of data management and visualization techniques for structural health monitoring using BIM and virtual or augmented reality. *J. Struct. Eng.* **2023**, *149*, [article number]. https://doi.org/10.1061/(ASCE)ST.1943-541X.0003498",
 "theiler2018": "Theiler, M.; Smarsly, K. IFC Monitor—An IFC schema extension for modeling structural health monitoring systems. *Adv. Eng. Inform.* **2018**, *37*, 54–65. https://doi.org/10.1016/j.aei.2018.04.011",
 "hu2024": "Hu, X.; Olgun, G.; Assaad, R.H. An intelligent BIM-enabled digital twin framework for real-time structural health monitoring using wireless IoT sensing, digital signal processing, and structural analysis. *Expert Syst. Appl.* **2024**, *252*, 124204. https://doi.org/10.1016/j.eswa.2024.124204",
 "gragnaniello2024": "Gragnaniello, C.; Mariniello, G.; Pastore, T.; Asprone, D. BIM-based design and setup of structural health monitoring systems. *Autom. Constr.* **2024**, *158*, 105245. https://doi.org/10.1016/j.autcon.2023.105245",
 "lee2018": "Lee, Y.-C.; Eastman, C.M.; Solihin, W. Logic for ensuring the data exchange integrity of building information models. *Autom. Constr.* **2018**, *85*, 249–262. https://doi.org/10.1016/j.autcon.2017.08.010",
 "lee2021": "Lee, Y.-C.; Eastman, C.M.; Solihin, W. Rules and validation processes for interoperable BIM data exchange. *J. Comput. Des. Eng.* **2021**, *8*, 97–114. https://doi.org/10.1093/jcde/qwaa064",
 "shafiq2022": "Shafiq, M.T.; Lockley, S.R. Application of signature-based matching for IFC model comparison. *Int. J. Constr. Manag.* **2022**, *22*, 1765–1774. https://doi.org/10.1080/15623599.2020.1742630",
 "ricothirion2026": "Rico Thirion, M.A.; Moghtadernejad, S.; Xu, Y.; Lounis, Z.; Chen, Q. Digital twin platform based on an identity-semantic-interaction framework to improve bridge management workflows. *Digit. Eng.* **2026**, *11*, 100111. https://doi.org/10.1016/j.dte.2026.100111",
 "wang1996": "Wang, R.Y.; Strong, D.M. Beyond accuracy: What data quality means to data consumers. *J. Manag. Inf. Syst.* **1996**, *12*, 5–33. https://doi.org/10.1080/07421222.1996.11518099",
 "celik2023": "Çelik, Y.; Petri, I.; Barati, M. Blockchain supported BIM data provenance for construction projects. *Comput. Ind.* **2023**, *144*, 103768. https://doi.org/10.1016/j.compind.2022.103768",
 "erripradeep2021": "Erri Pradeep, A.S.; Yiu, T.W.; Zou, Y.; Amor, R. Blockchain-aided information exchange records for design liability control and improved security. *Autom. Constr.* **2021**, *126*, 103667. https://doi.org/10.1016/j.autcon.2021.103667",
 "tavakoli2024": "Tavakoli, P.; Yitmen, I.; Sadri, H.; Taheri, A. Blockchain-based digital twin data provenance for predictive asset management in building facilities. *Smart Sustain. Built Environ.* **2024**, *13*, 4–21. https://doi.org/10.1108/SASBE-07-2023-0169",
 "ciccarese2013": "Ciccarese, P.; Soiland-Reyes, S.; Belhajjame, K.; Gray, A.J.G.; Goble, C.; Clark, T. PAV ontology: Provenance, authoring and versioning. *J. Biomed. Semant.* **2013**, *4*, 37. https://doi.org/10.1186/2041-1480-4-37",
 "sacks2018": "Sacks, R.; Kedar, A.; Borrmann, A.; Ma, L.; Brilakis, I.; Hüthwohl, P.; Daum, S.; Kattel, U.; Yosef, R.; Liebich, T.; et al. SeeBridge as next generation bridge inspection: Overview, information delivery manual and model view definition. *Autom. Constr.* **2018**, *90*, 134–145. https://doi.org/10.1016/j.autcon.2018.02.033",
 "wan2019": "Wan, C.; Zhou, Z.; Li, S.; Ding, Y.; Xu, Z.; Yang, Z.; Xia, Y.; Yin, F. Development of a bridge management system based on the building information modeling technology. *Sustainability* **2019**, *11*, 4583. https://doi.org/10.3390/su11174583",
 "shalabi2017": "Shalabi, F.; Turkan, Y. IFC BIM-based facility management approach to optimize data collection for corrective maintenance. *J. Perform. Constr. Facil.* **2017**, *31*, [article number]. https://doi.org/10.1061/(ASCE)CF.1943-5509.0000941",
 "liu2022": "Liu, K.; El-Gohary, N. Bridge deterioration knowledge ontology for supporting bridge document analytics. *J. Constr. Eng. Manag.* **2022**, *148*, [article number]. https://doi.org/10.1061/(ASCE)CO.1943-7862.0002210",
 "matarneh2022": "Matarneh, S.; Elghaish, F.; Pour Rahimian, F.; Dawood, N.; Edwards, D. Automated and interconnected facility management system: An open IFC cloud-based BIM solution. *Autom. Constr.* **2022**, *143*, 104569. https://doi.org/10.1016/j.autcon.2022.104569",
 "otranto2025": "Otranto, R.B.; Miceli Junior, G.; Pellanda, P.C. BIM-FM integration through openBIM: Solutions for interoperability towards efficient operations. *J. Inf. Technol. Constr.* **2025**, *30*, 298–318. https://doi.org/10.36680/j.itcon.2025.012",
 "godager2024": "Godager, B.; et al. Exploring the Enterprise BIM concept in practice: The case of asset management in a Norwegian hospital. *J. Inf. Technol. Constr.* **2024**, *29*, 549–572. https://doi.org/10.36680/j.itcon.2024.025 [complete author list]",
 "chatsuwan2025b": "Chatsuwan, M.; et al. BIM–FM interoperability through open standards: A critical literature review. *Architecture* **2025**, *5*, 74. https://doi.org/10.3390/architecture5030074 [complete author list]",
 "monfardini2023": "Monfardini, G.K.Q.; Salamon, J.S.; Barcellos, M.P. Use of competency questions in ontology engineering: A survey. In *Conceptual Modeling. ER 2023*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2023; pp. 45–64. https://doi.org/10.1007/978-3-031-47262-6_3",
 "jia2011": "Jia, Y.; Harman, M. An analysis and survey of the development of mutation testing. *IEEE Trans. Softw. Eng.* **2011**, *37*, 649–678. https://doi.org/10.1109/TSE.2010.62",
 "hevner2004": "Hevner, A.R.; March, S.T.; Park, J.; Ram, S. Design science in information systems research. *MIS Q.* **2004**, *28*, 75–106. https://doi.org/10.2307/25148625",
}

def fmt(nums):
    nums = sorted(set(nums)); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
        out.append(f"{nums[i]}–{nums[j]}" if j - i >= 2 else (f"{nums[i]},{nums[j]}" if j == i + 1 else f"{nums[i]}"))
        i = j + 1
    return "[" + ",".join(out) + "]"

text = SRC.read_text(encoding="utf-8")
order = {}
def repl(m):
    keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
    for k in keys:
        if k not in REFS: sys.exit(f"unknown key {k}")
        order.setdefault(k, len(order) + 1)
    return fmt([order[k] for k in keys])
text = re.sub(r"\[(@[^\]]+)\]", repl, text)
unused = set(REFS) - set(order)
if unused: print("UNUSED:", unused)
refs = "\n\n## References\n\n" + "\n".join(f"{n}. {REFS[k]}" for k, n in sorted(order.items(), key=lambda x: x[1]))
OUT.write_text(text + refs + "\n", encoding="utf-8")
print("refs", len(order), "->", OUT)
