'''
Unit tests for NexmdOuput
'''
import os
import pytest
from python_scripts.libnexmdoutput import NexmdOutput
import numpy as np

def setup_module(module):
    '''
    Switch to test directory
    '''
    os.chdir("tests/nexmdoutput")

def teardown_module(module):
    '''
    Return to main directory
    '''
    os.chdir("../..")

@pytest.fixture
def nexmdoutput():
    '''
    Creation of the Nexmd object
    '''
    return NexmdOutput('nexmd.out')

def test_find_es_energies(nexmdoutput):
    nexmdoutput.es_energies
    answer = np.array(
    [0.,             0.,             0.,             0.,             0.,             0.,
     0.,             0.,             0.,             0.,             0.,             0.,
     0.,             0.,             0.,             0.,             0.,             0.,
     0.,             0.,             0.,             0.,             0.,             0.,
     -1011.19336621, -1010.48303943, -1009.50699719, -1011.19336621, -1010.48303943,
     -1009.50699719, -1011.19336621, -1010.48303943, -1009.50699719, -1011.19336621,
     -1010.48303943, -1009.50699719, -1011.19374857, -1010.48336904, -1009.50729473,
     -1011.19374857, -1010.48336904, -1009.50729473, -1011.19374857, -1010.48336904,
     -1009.50729473, -1011.19374857, -1010.48336904, -1009.50729473, -1011.19492264,
     -1010.48431681, -1009.50823638, -1011.19492264, -1010.48431681, -1009.50823638,
     -1011.19492264, -1010.48431681, -1009.50823638, -1011.19492264, -1010.48431681,
     -1009.50823638, -1011.1968607,  -1010.48590561, -1009.50978047, -1011.1968607,
     -1010.48590561, -1009.50978047, -1011.1968607,  -1010.48590561, -1009.50978047,
     -1011.1968607,  -1010.48590561, -1009.50978047, -1011.19956019, -1010.48811752,
     -1009.51193029, -1011.19956019, -1010.48811752, -1009.51193029, -1011.19956019,
     -1010.48811752, -1009.51193029, -1011.19956019, -1010.48811752, -1009.51193029,
     -1011.20299469, -1010.49092436, -1009.5146679,  -1011.20299469, -1010.49092436,
     -1009.5146679,  -1011.20299469, -1010.49092436, -1009.5146679,  -1011.20299469,
     -1010.49092436, -1009.5146679,  -1011.20717359, -1010.49434043, -1009.51799335,
     -1011.20717359, -1010.49434043, -1009.51799335, -1011.20717359, -1010.49434043,
     -1009.51799335, -1011.20717359, -1010.49434043, -1009.51799335, -1011.20717359,
     -1010.49434043, -1009.51799335, -1011.21239747, -1010.49782812, -1009.5222498,
     -1011.21239747, -1010.49782812, -1009.5222498,  -1011.21239747, -1010.49782812,
     -1009.5222498,  -1011.21239747, -1010.49782812, -1009.5222498,  -1011.21795012,
     -1010.50241242, -1009.52665565, -1011.21795012, -1010.50241242, -1009.52665565,
     -1011.21795012, -1010.50241242, -1009.52665565, -1011.21795012, -1010.50241242,
     -1009.52665565, -1011.22418583, -1010.50748208, -1009.53160833, -1011.22418583,
     -1010.50748208, -1009.53160833, -1011.22418583, -1010.50748208, -1009.53160833,
     -1011.22418583, -1010.50748208, -1009.53160833, -1011.23105034, -1010.51305002,
     -1009.53705584])
    np.testing.assert_allclose(nexmdoutput.es_energies, answer)


def test_find_gs_energies(nexmdoutput):
    result = nexmdoutput.gs_energies
    answer = np.array(
        [-1014.55990789, -1014.55990789, -1014.55990789, -1014.55990789, -1014.55990789,
         -1014.55990789, -1014.55990789, -1014.55990789, -1014.55990789, -1014.56003514,
         -1014.56003514, -1014.56003514, -1014.56003514, -1014.56041533, -1014.56041533,
         -1014.56041533, -1014.56041533, -1014.56104379, -1014.56104379, -1014.56104379,
         -1014.56104379, -1014.5619128,  -1014.5619128,  -1014.5619128,  -1014.5619128,
         -1014.56299131, -1014.56299131, -1014.56299131, -1014.56299131, -1014.56430627,
         -1014.56430627, -1014.56430627, -1014.56430627, -1014.56586315, -1014.56586315,
         -1014.56586315, -1014.56586315, -1014.56586315, -1014.56755991, -1014.56755991,
         -1014.56755991, -1014.56755991, -1014.56941444, -1014.56941444, -1014.56941444,
        -1014.56941444, -1014.57140413, -1014.57140413, -1014.57140413, -1014.57140413])
    np.testing.assert_allclose(result, answer)

def test_find_omegas(nexmdoutput):
    result = nexmdoutput.omegas
    answer = np.array(
        [3.65209513e+00,   6.00980300e-05,   3.82515288e+00,   5.36758420e-05,
         5.27344595e+00,   5.79413731e-02,   3.61289438e+00,   2.90575639e-05,
         3.86513022e+00,   8.31239583e-05,   5.25495703e+00,   5.09927372e-02,
         3.43954923e+00,   1.25607755e-05,   4.02329344e+00,   9.24990833e-05,
         5.12153729e+00,   3.70806047e-02,   3.36797296e+00,   1.10257805e-05,
         4.07762201e+00,   8.94102392e-05,   5.05599071e+00,   3.50956818e-02,
         3.36673420e+00,   1.09500734e-05,   4.07669682e+00,   8.91058221e-05,
         5.05308576e+00,   3.50676974e-02,   3.36653889e+00,   1.09478246e-05,
         4.07687665e+00,   8.90980877e-05,   5.05291361e+00,   3.50628689e-02,
         3.36654168e+00,   1.09476918e-05,   4.07686845e+00,   8.90974533e-05,
         5.05291070e+00,   3.50629371e-02,   3.36654168e+00,   1.09476918e-05,
         4.07686845e+00,   8.90974533e-05,   5.05291070e+00,   3.50629371e-02,
         3.36632128e+00,   1.09417559e-05,   4.07665000e+00,   8.90818181e-05,
         5.05277721e+00,   3.50486088e-02,   3.36628667e+00,   1.09410174e-05,
         4.07666661e+00,   8.90796737e-05,   5.05274118e+00,   3.50478499e-02,
         3.36628656e+00,   1.09409949e-05,   4.07666609e+00,   8.90795798e-05,
         5.05274040e+00,   3.50478465e-02,   3.36628656e+00,   1.09409949e-05,
         4.07666609e+00,   8.90795798e-05,   5.05274040e+00,   3.50478465e-02,
         3.36560942e+00,   1.09233280e-05,   4.07604405e+00,   8.90201691e-05,
         5.05230416e+00,   3.50033631e-02,   3.36549311e+00,   1.09207830e-05,
         4.07610021e+00,   8.90126228e-05,   5.05218161e+00,   3.50008408e-02,
         3.36549269e+00,   1.09207066e-05,   4.07609852e+00,   8.90123041e-05,
         5.05217895e+00,   3.50008284e-02,   3.36549269e+00,   1.09207066e-05,
         4.07609852e+00,   8.90123041e-05,   5.05217895e+00,   3.50008284e-02,
         3.36437286e+00,   1.08918238e-05,   4.07504968e+00,   8.89173121e-05,
         5.05146619e+00,   3.49273822e-02,   3.36418367e+00,   1.08877341e-05,
         4.07514102e+00,   8.89051630e-05,   5.05126755e+00,   3.49232969e-02,
         3.36418309e+00,   1.08876118e-05,   4.07513818e+00,   8.89046498e-05,
         5.05126332e+00,   3.49232792e-02,   3.36418309e+00,   1.08876118e-05,
         4.07513818e+00,   8.89046498e-05,   5.05126332e+00,   3.49232792e-02,
         3.36261748e+00,   1.08472704e-05,   4.07367199e+00,   8.87722506e-05,
         5.05026561e+00,   3.48209440e-02,   3.36235330e+00,   1.08415981e-05,
         4.07379933e+00,   8.87552738e-05,   5.04998830e+00,   3.48152869e-02,
         3.36235261e+00,   1.08414301e-05,   4.07379528e+00,   8.87545645e-05,
         5.04998251e+00,   3.48152650e-02,   3.36235261e+00,   1.08414301e-05,
         4.07379528e+00,   8.87545645e-05,   5.04998251e+00,   3.48152650e-02,
         3.36033573e+00,   1.07892104e-05,   4.07190543e+00,   8.85836534e-05,
         5.04868285e+00,   3.46846040e-02,   3.35999703e+00,   1.07821376e-05,
         4.07207264e+00,   8.85617627e-05,   5.04833047e+00,   3.46774076e-02,
         3.35999662e+00,   1.07819287e-05,   4.07206695e+00,   8.85608603e-05,
         5.04832341e+00,   3.46773908e-02,   3.35999662e+00,   1.07819287e-05,
         4.07206695e+00,   8.85608603e-05,   5.04832341e+00,   3.46773908e-02,
         3.35754594e+00,   1.07194752e-05,   4.06977431e+00,   8.83527075e-05,
         5.04675418e+00,   3.45187418e-02,   3.35713320e+00,   1.07107911e-05,
         4.06997257e+00,   8.83261447e-05,   5.04632143e+00,   3.45101143e-02,
         3.35713269e+00,   1.07105406e-05,   4.06996584e+00,   8.83250696e-05,
         5.04631293e+00,   3.45100926e-02,   3.35713269e+00,   1.07105406e-05,
         4.06996584e+00,   8.83250696e-05,   5.04631293e+00,   3.45100926e-02,
         3.35428762e+00,   1.06421470e-05,   4.06722227e+00,   8.80894524e-05,
         5.04451835e+00,   3.43249460e-02,   3.35344145e+00,   1.06225328e-05,
         4.06807719e+00,   8.80719060e-05,   5.04361503e+00,   3.43068594e-02,
         3.35346904e+00,   1.06219244e-05,   4.06803090e+00,   8.80708197e-05,
         5.04361523e+00,   3.43074287e-02,   3.35346568e+00,   1.06219138e-05,
         4.06803503e+00,   8.80708567e-05,   5.04361335e+00,   3.43073517e-02,
         3.35346568e+00,   1.06219138e-05,   4.06803503e+00,   8.80708567e-05,
         5.04361335e+00,   3.43073517e-02,   3.35014880e+00,   1.05390421e-05,
         4.06492278e+00,   8.77883879e-05,   5.04147549e+00,   3.40954267e-02,
         3.34960882e+00,   1.05287560e-05,   4.06515734e+00,   8.77565962e-05,
         5.04091374e+00,   3.40845681e-02,   3.34960979e+00,   1.05284627e-05,
         4.06514749e+00,   8.77552760e-05,   5.04090425e+00,   3.40845741e-02,
         3.34960979e+00,   1.05284627e-05,   4.06514749e+00,   8.77552760e-05,
         5.04090425e+00,   3.40845741e-02,   3.34585747e+00,   1.04352167e-05,
         4.06164364e+00,   8.74338796e-05,   5.03847551e+00,   3.38472451e-02,
         3.34522732e+00,   1.04226269e-05,   4.06194415e+00,   8.73932961e-05,
         5.03781710e+00,   3.38347862e-02,   3.34522860e+00,   1.04222833e-05,
         4.06193235e+00,   8.73917743e-05,   5.03780611e+00,   3.38347953e-02,
         3.34522860e+00,   1.04222833e-05,   4.06193235e+00,   8.73917743e-05,
         5.03780611e+00,   3.38347953e-02,   3.34105154e+00,   1.03195588e-05,
         4.05803514e+00,   8.70329096e-05,   5.03509031e+00,   3.35731665e-02,
         3.34035152e+00,   1.03058385e-05,   4.05836781e+00,   8.69877826e-05,
         5.03435968e+00,   3.35596346e-02,   3.34035379e+00,   1.03054728e-05,
         4.05835411e+00,   8.69861445e-05,   5.03434829e+00,   3.35596605e-02,
         3.34035379e+00,   1.03054728e-05,   4.05835411e+00,   8.69861445e-05,
         5.03434829e+00,   3.35596605e-02])
    np.testing.assert_allclose(result, answer)


def test_find_orbitals(nexmdoutput):
    result = nexmdoutput.orbitals
    answer = np.array(
        [-44.1131958,  -38.1469186,  -32.4494069,  -24.8807713,  -20.1005064,  -19.581519,
         -19.2794978,  -14.271313,   -14.0414656,  -12.6607704,  -12.3670685,
         -12.3509275,   -0.20015145,   0.97925222,   3.44199704,   3.62962732,
         4.09005058,   5.4694166,    6.78409381, -44.1123236,  -38.1462812,  -32.449264,
         -24.8807177,  -20.1004417,  -19.5812229,  -19.279076,   -14.2712487,
         -14.0413678,  -12.6607272,  -12.3671122,  -12.3508203,   -0.20041421,
         0.97917048,   3.44192254,   3.62955387,   4.08987274,   5.46927982,
         6.78380782, -44.1095623,  -38.1442285,  -32.4488261,  -24.8805244,
         -20.1001594,  -19.5802854,  -19.2777258,  -14.2710626,  -14.0410736,
         -12.6605273,  -12.3671813,  -12.3504169,   -0.20112044,   0.97897012,
         3.44167965,   3.62931388,   4.0892921,    5.46897674,   6.78304863,
         -44.1050257,  -38.1408683,  -32.4481,     -24.8802153,  -20.0997247,
         -19.5787445,  -19.2755126,  -14.2707495,  -14.0405841,  -12.660223,   -12.367322,
         -12.3497778,   -0.20232826,   0.97862004,   3.44128505,   3.62892427,
         4.08834732,   5.46842837,   6.78174443, -44.0986849,  -38.1361704,
         -32.4470879,  -24.8797844,  -20.0991164,  -19.5765913,  -19.2724196,
         -14.2703132,  -14.0399013,  -12.6597982,  -12.3675181,  -12.3488843,   -0.204017,
         0.97812917,   3.44073376,   3.62838014,   4.08702754,   5.4676608,
         6.7799199,  -44.0905794,  -38.1301644,  -32.4458457,  -24.8792664,
         -20.0983575,  -19.5738701,  -19.2684854,  -14.2698083,  -14.0391121,
         -12.6592752,  -12.3677932,  -12.3477526,   -0.2062149,    0.97745231,
         3.43996887,   3.62758833,   4.08526526,   5.46664423,   6.77754904,
         -44.0806659,  -38.1228126,  -32.4442725,  -24.8785961,  -20.0974018,
         -19.5705059,  -19.2636508,  -14.2691306,  -14.0380492,  -12.6586133,
         -12.3680956,  -12.3463549,   -0.2088564,    0.97668077,   3.43911019,
         3.62674138,   4.08320747,   5.46543873,   6.77468979, -44.0691018,
         -38.1142672,  -32.4424734,  -24.8778977,  -20.0963803,  -19.5666114,
         -19.2580574,  -14.2683539,  -14.0368175,  -12.6579564,  -12.3685525,
         -12.3448739,   -0.21207874,   0.97572628,   3.43809436,   3.6257433,
         4.08077773,   5.46390092,   6.77122257, -44.0556706,  -38.1042904,
         -32.4403499,  -24.8769873,  -20.0950673,  -19.5620505,  -19.2515036,
         -14.2674341,  -14.0353786,  -12.6570538,  -12.3689422,  -12.3429718,
         -0.21564596,   0.97468789,   3.43694926,   3.62461316,   4.0780113,
         5.46226929,   6.76735204, -44.0405307,  -38.0930389,  -32.437981,   -24.8759765,
         -20.0935918,  -19.5569209,  -19.2441242,  -14.266416,   -14.0337729,
         -12.6560517,  -12.3693904,  -12.3408347,   -0.21968545,   0.97349355,
         3.43564879,   3.62333243,   4.07488835,   5.46040835,   6.76296032,
         -44.0236953,  -38.0805162,  -32.4353622,  -24.8748585,  -20.0919434,
         -19.5512207,  -19.2359203,  -14.2652918,  -14.0319954,  -12.6549415,
         -12.3698818, -12.3384569,   -0.2241796,    0.97215825,   3.43420817,
         3.62191473, 4.07142528,   5.45832964,   6.75806534])
    np.testing.assert_allclose(result, answer)
