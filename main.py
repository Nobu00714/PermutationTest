import numpy as np

def permutation_test(array1, array2, num_permutations):
    """
    Permutation Testを実行する関数

    Parameters:
    - array1: 1つ目の配列
    - array2: 2つ目の配列
    - num_permutations: 並べ替えの回数

    Returns:
    - p_value: Permutation Testのp値
    """

    # 2つの配列を結合して全体の配列を作成
    combined_array = np.concatenate([array1, array2])

    # 実際の統計量の計算
    actual_statistic = np.mean(array1) - np.mean(array2)

    # パーミュテーションテストの実行
    permutation_stats = []
    for _ in range(num_permutations):
        # 配列をランダムに並べ替え
        np.random.shuffle(combined_array)

        # シャッフルされた配列を2つのグループに分割
        permuted_array1 = combined_array[:len(array1)]
        permuted_array2 = combined_array[len(array1):]

        # シャッフルされた統計量の計算
        permuted_statistic = np.mean(permuted_array1) - np.mean(permuted_array2)
        permutation_stats.append(permuted_statistic)

    # パーミュテーション分布からp値の計算
    p_value = (np.abs(permutation_stats) >= np.abs(actual_statistic)).mean()

    return p_value

# テストデータ
LinearTPnAccurate = np.array([12.29170624,21.1298338,23.56428188,16.3423757,21.6288433,17.15583967,20.23409338,18.50230694,30.45837519,18.6606074,12.47453477,22.99646673])
LinearTPnNeutral = np.array([20.39777999,41.1652159,35.79649402,20.50892481,29.57106658,27.03161857,33.14684219,38.83195145,41.88448457,27.05803963,39.62318438,57.23351968])
LinearTPnFast = np.array([53.99327967,61.17793307,61.60804374,67.38269949,62.53035634,45.5351695,51.84052319,61.08732944,85.42244904,37.71074904,68.13016207,93.84625305
])

LinearTPweAccurate = np.array([42.38010252,79.50657635,81.82639803,68.90999398,86.02534999,62.67963682,60.38639079,70.63169905,110.542182,57.99500532,51.01884131,85.81198809])
LinearTPweNeutral = np.array([71.54652796,121.9907782,112.5694093,67.62157182,100.4652616,84.83359908,119.2892964,113.1045154,133.8828025,60.1793524,115.0657102,126.2014791])
LinearTPweFast = np.array([112.2373432,169.5762732,172.533608,143.1717088,168.3496095,114.96186,139.6547309,159.4223811,214.4590202,90.92715775,182.9190548,169.8384628])

LinearTPeAccurate = np.array([42.79107088,80.65695694,83.13175028,69.49897906,87.16228397,63.41913264,60.96500001,71.67001169,112.4001206,58.55691196,51.50172622,87.07583259])
LinearTPeNeutral = np.array([72.55119743,123.7224755,115.7897504,68.3559573,102.0738774,86.06965266,120.9321669,114.8271964,136.6283332,60.8909926,117.2360352,128.8270765])
LinearTPeFast = np.array([114.4535089,173.1389097,178.3844379,146.2878705,171.823186,117.2175144,141.9364663,163.7971103,220.5487458,92.49312675,187.1874969,175.3192194])

CircularTPnAccurate = np.array([8.704959342,7.594292802,6.678099972,8.018092274,11.3813446,7.692609847,8.085176985,8.14090137,14.09109851,13.51040609,9.444598124,8.545056252])
CircularTPnNeutral = np.array([14.07157085,11.05196186,12.35147838,13.54130878,12.79286013,10.48829318,11.15197098,13.13243903,15.7216673,15.26972618,18.27113959,13.45045178])
CircularTPnFast = np.array([31.96990019,23.57084713,25.65877625,31.36870295,25.36007134,15.08424721,21.20912802,27.54514949,29.57720204,25.16476666,37.51615655,31.71905306])

CircularTPweAccurate = np.array([21.63116275,19.89049058,15.59618893,21.7579074,24.06220436,20.33890313,19.27072456,21.34851681,29.19826723,26.77522734,32.48443791,20.76486255])
CircularTPweNeutral = np.array([28.89100054,24.03498635,22.15723,26.73716001,23.58605368,22.66697457,19.99183551,26.5330009,30.75437429,27.00258627,32.66140645,21.90877472])
CircularTPweFast = np.array([35.84905563,33.86711547,31.52013021,41.1258019,32.67486045,24.38513981,29.96171938,36.92629409,43.26759993,30.93176147,43.91560322,33.30900526])

CircularTPeAccurate = np.array([19.7623952,18.76388508,14.65105831,21.43954597,23.13154922,18.38200563,18.39140188,18.87576635,28.05416919,25.28464202,28.53362335,18.84554379])
CircularTPeNeutral = np.array([27.4981203,23.3546875,21.25722331,26.10763998,23.13150227,21.82505503,19.6120263,23.77262367,29.49475682,25.58037755,31.86252505,20.38076231])
CircularTPeFast = np.array([34.33436344,33.65992901,30.24539193,39.88559375,32.16435371,22.83724261,28.87928533,34.97624624,41.98052521,29.70520345,42.66494717,31.74187973])

SineWaveTPnAccurate = np.array([6.647605004,6.314303989,7.34989274,6.365861255,9.112706348,6.779442247,5.932344738,8.68437735,12.6066719,6.189867115,4.535489026,5.736605951])
SineWaveTPnNeutral = np.array([8.290201146,7.340083083,11.1228761,12.02123352,10.22394746,7.251213008,7.377193994,13.44798552,12.29072494,8.586414045,9.345266362,10.77805935])
SineWaveTPnFast = np.array([17.40493448,22.08459935,19.86326917,21.82098168,16.54363953,10.42071252,16.23473953,20.9176788,18.68113963,15.68895958,17.84159798,20.43904805])

SineWaveTPweAccurate = np.array([22.83109437,24.87421473,22.3657674,26.36950184,29.59111706,24.12658679,21.59504089,26.53186604,38.10531759,22.67194931,20.76828017,20.08107673])
SineWaveTPweNeutral = np.array([23.24755931,23.54074017,27.69436814,28.54056179,28.85861709,21.55816773,20.7971559,32.54928515,33.1028987,25.33095967,27.72715776,24.99976814])
SineWaveTPweFast = np.array([29.00338179,36.62016674,30.63579846,34.40407729,35.29295915,28.88718818,25.58736945,40.97523699,39.33960076,31.69183379,38.11910597,28.69483748])

SineWaveTPeAccurate = np.array([22.62019734,24.46736224,22.0632565,25.9379266,28.94682332,23.77448771,21.38756765,26.06939435,37.40101017,22.39669244,20.70110992,19.87887004])
SineWaveTPeNeutral = np.array([22.65140009,23.10688784,27.18818778,27.64843729,28.18758027,21.07551076,20.2660106,32.04697199,32.40094366,25.22872068,27.23147644,24.30382785])
SineWaveTPeFast = np.array([27.94397189,35.74676736,30.21565083,33.27270676,34.55020261,28.41620773,24.65181075,40.50857677,38.32838757,31.21329304,37.58281246,27.8990459])

# Permutation Testの実行
num_permutations = 1000000

print("Linear")
print("TPn")
p_value = permutation_test(LinearTPnAccurate, LinearTPnNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(LinearTPnNeutral, LinearTPnFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(LinearTPnAccurate, LinearTPnFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPwe")
p_value = permutation_test(LinearTPweAccurate, LinearTPweNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(LinearTPweNeutral, LinearTPweFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(LinearTPweAccurate, LinearTPweFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPe")
p_value = permutation_test(LinearTPeAccurate, LinearTPeNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(LinearTPeNeutral, LinearTPeFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(LinearTPeAccurate, LinearTPeFast, num_permutations)
print("Accurate Fast:", p_value)

print("Circular")
print("TPn")
p_value = permutation_test(CircularTPnAccurate, CircularTPnNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(CircularTPnNeutral, CircularTPnFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(CircularTPnAccurate, CircularTPnFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPwe")
p_value = permutation_test(CircularTPweAccurate, CircularTPweNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(CircularTPweNeutral, CircularTPweFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(CircularTPweAccurate, CircularTPweFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPe")
p_value = permutation_test(CircularTPeAccurate, CircularTPeNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(CircularTPeNeutral, CircularTPeFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(CircularTPeAccurate, CircularTPeFast, num_permutations)
print("Accurate Fast:", p_value)

print("SineWave")
print("TPn")
p_value = permutation_test(SineWaveTPnAccurate, SineWaveTPnNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(SineWaveTPnNeutral, SineWaveTPnFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(SineWaveTPnAccurate, SineWaveTPnFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPwe")
p_value = permutation_test(SineWaveTPweAccurate, SineWaveTPweNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(SineWaveTPweNeutral, SineWaveTPweFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(SineWaveTPweAccurate, SineWaveTPweFast, num_permutations)
print("Accurate Fast:", p_value)

print("TPe")
p_value = permutation_test(SineWaveTPeAccurate, SineWaveTPeNeutral, num_permutations)
print("Accurate Neutral:", p_value)
p_value = permutation_test(SineWaveTPeNeutral, SineWaveTPeFast, num_permutations)
print("Neutral Fast:", p_value)
p_value = permutation_test(SineWaveTPeAccurate, SineWaveTPeFast, num_permutations)
print("Accurate Fast:", p_value)