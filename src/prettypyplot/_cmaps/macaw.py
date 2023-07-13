"""Macaw colormap.

This is self-defined colormap similar to viridis generated with viscm.

BSD 3-Clause License
Copyright (c) 2020-2021, Daniel Nagel
All rights reserved.

"""
# ~~~ IMPORT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from matplotlib import colors as clr

# ~~~ CMAP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CM_MACAW_DATA = [
    [0.19058156, 0.05187944, 0.50289419],
    [0.18954119, 0.05806460, 0.50959124],
    [0.18847439, 0.06392324, 0.51625442],
    [0.18730591, 0.06950876, 0.52298851],
    [0.18602844, 0.07486335, 0.52979742],
    [0.18462615, 0.08001914, 0.53669617],
    [0.18310049, 0.08500270, 0.54367455],
    [0.18143568, 0.08983444, 0.55074552],
    [0.17962612, 0.09453176, 0.55790684],
    [0.17765937, 0.09910869, 0.56516442],
    [0.17553274, 0.10357790, 0.57251009],
    [0.17322480, 0.10794869, 0.57995868],
    [0.17073274, 0.11223064, 0.58749950],
    [0.16803817, 0.11643087, 0.59513984],
    [0.16512046, 0.12055543, 0.60288710],
    [0.16196874, 0.12461064, 0.61073458],
    [0.15855956, 0.12860117, 0.61868760],
    [0.15487150, 0.13253595, 0.62673743],
    [0.15083313, 0.13656790, 0.63463945],
    [0.14631781, 0.14075836, 0.64234417],
    [0.14125338, 0.14513510, 0.64979801],
    [0.13554961, 0.14972929, 0.65693645],
    [0.12909038, 0.15457590, 0.66368238],
    [0.12175680, 0.15973889, 0.66986869],
    [0.11335556, 0.16526020, 0.67537829],
    [0.10368472, 0.17121161, 0.67997378],
    [0.09249210, 0.17766098, 0.68337230],
    [0.07951637, 0.18464906, 0.68525372],
    [0.06463115, 0.19217895, 0.68522460],
    [0.04792058, 0.20011790, 0.68310082],
    [0.03049412, 0.20821928, 0.67897102],
    [0.01673951, 0.21619067, 0.67327099],
    [0.00758631, 0.22382123, 0.66652851],
    [0.00269288, 0.23100257, 0.65925719],
    [0.00158900, 0.23772009, 0.65176198],
    [0.00373727, 0.24400003, 0.64423947],
    [0.00863564, 0.24987935, 0.63682943],
    [0.01592935, 0.25540460, 0.62957975],
    [0.02526202, 0.26061394, 0.62255010],
    [0.03644893, 0.26554722, 0.61572782],
    [0.04808908, 0.27026523, 0.60918586],
    [0.05799278, 0.27486365, 0.60295340],
    [0.06662470, 0.27935889, 0.59700827],
    [0.07427470, 0.28376252, 0.59134582],
    [0.08112675, 0.28808472, 0.58596186],
    [0.08730584, 0.29233460, 0.58085244],
    [0.09290131, 0.29652027, 0.57601351],
    [0.09797941, 0.30064901, 0.57144114],
    [0.10258160, 0.30472823, 0.56713256],
    [0.10675656, 0.30876306, 0.56308197],
    [0.11053742, 0.31275862, 0.55928464],
    [0.11394960, 0.31671971, 0.55573576],
    [0.11701374, 0.32065082, 0.55242977],
    [0.11974671, 0.32455583, 0.54936183],
    [0.12216208, 0.32843854, 0.54652563],
    [0.12427086, 0.33230225, 0.54391559],
    [0.12608149, 0.33615017, 0.54152519],
    [0.12760054, 0.33998509, 0.53934850],
    [0.12883214, 0.34380985, 0.53737833],
    [0.12977917, 0.34762677, 0.53560881],
    [0.13044216, 0.35143829, 0.53403281],
    [0.13081987, 0.35524663, 0.53264340],
    [0.13090933, 0.35905383, 0.53143386],
    [0.13069151, 0.36286329, 0.53039973],
    [0.13017051, 0.36667556, 0.52953264],
    [0.12933735, 0.37049236, 0.52882549],
    [0.12818021, 0.37431527, 0.52827171],
    [0.12668440, 0.37814575, 0.52786479],
    [0.12480372, 0.38198787, 0.52760245],
    [0.12253981, 0.38584057, 0.52747446],
    [0.11986539, 0.38970506, 0.52747450],
    [0.11672338, 0.39358453, 0.52759944],
    [0.11307467, 0.39747956, 0.52784292],
    [0.10925654, 0.40136808, 0.52809131],
    [0.10577722, 0.40522092, 0.52820478],
    [0.10265366, 0.40903876, 0.52819928],
    [0.09991901, 0.41282127, 0.52808615],
    [0.09772109, 0.41656205, 0.52784963],
    [0.09601252, 0.42026534, 0.52751928],
    [0.09486795, 0.42392856, 0.52709424],
    [0.09434407, 0.42754991, 0.52657606],
    [0.09438345, 0.43113307, 0.52598810],
    [0.09509197, 0.43467296, 0.52531564],
    [0.09635834, 0.43817505, 0.52458762],
    [0.09822100, 0.44163693, 0.52379717],
    [0.10061058, 0.44506123, 0.52295921],
    [0.10350092, 0.44844829, 0.52207617],
    [0.10683689, 0.45179979, 0.52115587],
    [0.11057809, 0.45511651, 0.52020322],
    [0.11465448, 0.45840131, 0.51922642],
    [0.11905762, 0.46165331, 0.51822257],
    [0.12367500, 0.46487844, 0.51721006],
    [0.12856585, 0.46807181, 0.51617148],
    [0.13360141, 0.47124106, 0.51513069],
    [0.13878242, 0.47438574, 0.51408241],
    [0.14410420, 0.47750565, 0.51302374],
    [0.14949549, 0.48060578, 0.51196760],
    [0.15495525, 0.48368624, 0.51091074],
    [0.16049172, 0.48674623, 0.50984867],
    [0.16604880, 0.48979059, 0.50879143],
    [0.17161672, 0.49282052, 0.50773901],
    [0.17720503, 0.49583556, 0.50668647],
    [0.18280577, 0.49883682, 0.50563324],
    [0.18839033, 0.50182730, 0.50458623],
    [0.19395551, 0.50480816, 0.50354212],
    [0.19949671, 0.50778037, 0.50250156],
    [0.20501472, 0.51074450, 0.50146239],
    [0.21051968, 0.51370023, 0.50041836],
    [0.21598949, 0.51665032, 0.49937626],
    [0.22142483, 0.51959567, 0.49833147],
    [0.22682313, 0.52253702, 0.49728571],
    [0.23218567, 0.52547515, 0.49623434],
    [0.23751130, 0.52841072, 0.49517762],
    [0.24280071, 0.53134438, 0.49411291],
    [0.24805496, 0.53427675, 0.49303727],
    [0.25327337, 0.53720832, 0.49195140],
    [0.25845821, 0.54013961, 0.49085082],
    [0.26361046, 0.54307107, 0.48973375],
    [0.26873137, 0.54600306, 0.48859829],
    [0.27382187, 0.54893593, 0.48744343],
    [0.27888467, 0.55186996, 0.48626493],
    [0.28392435, 0.55480540, 0.48505484],
    [0.28900262, 0.55773063, 0.48382426],
    [0.29413974, 0.56064222, 0.48256931],
    [0.29933930, 0.56353921, 0.48128992],
    [0.30460443, 0.56642066, 0.47998659],
    [0.30993814, 0.56928561, 0.47865969],
    [0.31534355, 0.57213311, 0.47730916],
    [0.32082389, 0.57496214, 0.47593445],
    [0.32638070, 0.57777180, 0.47453762],
    [0.33201619, 0.58056111, 0.47311926],
    [0.33773289, 0.58332911, 0.47167917],
    [0.34353170, 0.58607490, 0.47021948],
    [0.34941643, 0.58879691, 0.46874323],
    [0.35539061, 0.59149377, 0.46725090],
    [0.36144955, 0.59416573, 0.46574422],
    [0.36759411, 0.59681194, 0.46422404],
    [0.37382414, 0.59943167, 0.46269235],
    [0.38013888, 0.60202427, 0.46115158],
    [0.38653831, 0.60458903, 0.45960306],
    [0.39302085, 0.60712544, 0.45804979],
    [0.39958560, 0.60963295, 0.45649371],
    [0.40623102, 0.61211111, 0.45493730],
    [0.41295537, 0.61455952, 0.45338306],
    [0.41975689, 0.61697782, 0.45183335],
    [0.42663689, 0.61936474, 0.45029309],
    [0.43359518, 0.62171941, 0.44876629],
    [0.44062362, 0.62404336, 0.44725157],
    [0.44771948, 0.62633657, 0.44575159],
    [0.45488058, 0.62859894, 0.44426831],
    [0.46210390, 0.63083057, 0.44280444],
    [0.46938718, 0.63303146, 0.44136181],
    [0.47672758, 0.63520176, 0.43994273],
    [0.48412245, 0.63734164, 0.43854929],
    [0.49156972, 0.63945118, 0.43718289],
    [0.49906579, 0.64153081, 0.43584635],
    [0.50660936, 0.64358054, 0.43454029],
    [0.51420161, 0.64559928, 0.43327054],
    [0.52183597, 0.64758876, 0.43203524],
    [0.52951071, 0.64954923, 0.43083420],
    [0.53722227, 0.65148137, 0.42966989],
    [0.54496971, 0.65338524, 0.42854256],
    [0.55275129, 0.65526109, 0.42745314],
    [0.56056486, 0.65710934, 0.42640291],
    [0.56840818, 0.65893047, 0.42539318],
    [0.57628132, 0.66072433, 0.42442350],
    [0.58418211, 0.66249141, 0.42349515],
    [0.59210876, 0.66423213, 0.42260915],
    [0.60005987, 0.66594682, 0.42176622],
    [0.60803548, 0.66763539, 0.42096604],
    [0.61603390, 0.66929830, 0.42020960],
    [0.62405442, 0.67093569, 0.41949718],
    [0.63209596, 0.67254786, 0.41882938],
    [0.64015622, 0.67413550, 0.41820762],
    [0.64823610, 0.67569830, 0.41763113],
    [0.65633376, 0.67723686, 0.41710106],
    [0.66445362, 0.67874915, 0.41662226],
    [0.67259044, 0.68023734, 0.41619149],
    [0.68074383, 0.68170156, 0.41580848],
    [0.68891283, 0.68314217, 0.41547379],
    [0.69709647, 0.68455952, 0.41518798],
    [0.70529471, 0.68595364, 0.41495099],
    [0.71350597, 0.68732515, 0.41476373],
    [0.72173070, 0.68867392, 0.41462583],
    [0.73000998, 0.68998466, 0.41450613],
    [0.73829277, 0.69128478, 0.41430330],
    [0.74659018, 0.69257004, 0.41401107],
    [0.75491011, 0.69383731, 0.41362380],
    [0.76324925, 0.69508807, 0.41313892],
    [0.77160955, 0.69632176, 0.41254970],
    [0.77998812, 0.69753979, 0.41185185],
    [0.78838979, 0.69874052, 0.41103463],
    [0.79681252, 0.69992514, 0.41009100],
    [0.80525224, 0.70109576, 0.40901451],
    [0.81371833, 0.70224898, 0.40778666],
    [0.82218335, 0.70339787, 0.40640285],
    [0.83066641, 0.70453472, 0.40484057],
    [0.83916828, 0.70565993, 0.40308387],
    [0.84768783, 0.70677497, 0.40111375],
    [0.85619810, 0.70789456, 0.39890385],
    [0.86470812, 0.70901596, 0.39642621],
    [0.87321308, 0.71014341, 0.39364913],
    [0.88168496, 0.71129398, 0.39052555],
    [0.89011144, 0.71247634, 0.38702014],
    [0.89847380, 0.71370378, 0.38307790],
    [0.90671642, 0.71500913, 0.37864563],
    [0.91477514, 0.71643005, 0.37367920],
    [0.92257363, 0.71801064, 0.36815123],
    [0.92998748, 0.71981955, 0.36207705],
    [0.93690366, 0.72191679, 0.35554231],
    [0.94320799, 0.72435942, 0.34871695],
    [0.94880339, 0.72719287, 0.34182459],
    [0.95368361, 0.73041301, 0.33507907],
    [0.95791320, 0.73397897, 0.32863186],
    [0.96156968, 0.73784557, 0.32255616],
    [0.96474147, 0.74196301, 0.31687987],
    [0.96751348, 0.74628535, 0.31158078],
    [0.96995295, 0.75077649, 0.30662850],
    [0.97208994, 0.75542021, 0.30199675],
    [0.97401256, 0.76017018, 0.29763355],
    [0.97570333, 0.76503552, 0.29352109],
    [0.97723918, 0.76997570, 0.28962258],
    [0.97860610, 0.77499845, 0.28591054],
    [0.97982931, 0.78009040, 0.28236357],
    [0.98093791, 0.78523620, 0.27896562],
    [0.98193715, 0.79043341, 0.27569295],
    [0.98283325, 0.79567880, 0.27252878],
    [0.98359296, 0.80099206, 0.26937692],
    [0.98434061, 0.80631328, 0.26612485],
    [0.98507077, 0.81164585, 0.26275080],
    [0.98578487, 0.81698903, 0.25925215],
    [0.98648115, 0.82234384, 0.25561899],
    [0.98715714, 0.82771170, 0.25183903],
    [0.98782455, 0.83308608, 0.24793183],
    [0.98847119, 0.83847386, 0.24386181],
    [0.98909511, 0.84387611, 0.23961519],
    [0.98970390, 0.84928864, 0.23520039],
    [0.99029313, 0.85471390, 0.23059595],
    [0.99085534, 0.86015592, 0.22577035],
    [0.99140774, 0.86560540, 0.22075415],
    [0.99192644, 0.87107513, 0.21546858],
    [0.99243373, 0.87655320, 0.20995525],
    [0.99291025, 0.88204984, 0.20413959],
    [0.99336479, 0.88756033, 0.19802097],
    [0.99379712, 0.89308477, 0.19156975],
    [0.99420035, 0.89862665, 0.18472928],
    [0.99457573, 0.90418523, 0.17745945],
    [0.99492529, 0.90975938, 0.16971376],
    [0.99524338, 0.91535187, 0.16140537],
    [0.99552698, 0.92096406, 0.15243487],
    [0.99578712, 0.92659034, 0.14273134],
    [0.99600800, 0.93223841, 0.13207549],
    [0.99619108, 0.93790735, 0.12024698],
    [0.99632933, 0.94360034, 0.10686924],
    [0.99641293, 0.94932183, 0.09131728],
    [0.99632399, 0.95512747, 0.07162400],
]


def _macaw():
    return clr.LinearSegmentedColormap.from_list("macaw", CM_MACAW_DATA)
