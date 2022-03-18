# This file is generated from pydcs_export.lua

from dcs.country import Country
import dcs.vehicles as vehicles
import dcs.planes as planes
import dcs.helicopters as helicopters
import dcs.ships as ships


class Russia(Country):
    id = 0
    name = "Russia"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            AA8 = vehicles.Unarmed.AA8
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            T_90 = vehicles.Armor.T_90
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_33 = planes.Su_33
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        Su_25TM = planes.Su_25TM
        Su_25T = planes.Su_25T
        MiG_31 = planes.MiG_31
        MiG_27K = planes.MiG_27K
        Su_30 = planes.Su_30
        Tu_160 = planes.Tu_160
        Su_34 = planes.Su_34
        Tu_95MS = planes.Tu_95MS
        Tu_142 = planes.Tu_142
        MiG_25PD = planes.MiG_25PD
        Tu_22M3 = planes.Tu_22M3
        A_50 = planes.A_50
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_17M4 = planes.Su_17M4
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_33,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.Su_25TM,
        Plane.Su_25T,
        Plane.MiG_31,
        Plane.MiG_27K,
        Plane.Su_30,
        Plane.Tu_160,
        Plane.Su_34,
        Plane.Tu_95MS,
        Plane.Tu_142,
        Plane.MiG_25PD,
        Plane.Tu_22M3,
        Plane.A_50,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_17M4,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        Mi_28N = helicopters.Mi_28N
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.Mi_28N,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        KUZNECOW = ships.KUZNECOW
        MOSCOW = ships.MOSCOW
        PIOTR = ships.PIOTR
        ELNYA = ships.ELNYA
        ALBATROS = ships.ALBATROS
        REZKY = ships.REZKY
        MOLNIYA = ships.MOLNIYA
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        ZWEZDNY = ships.ZWEZDNY
        NEUSTRASH = ships.NEUSTRASH
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        CV_1143_5 = ships.CV_1143_5

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Russia, self).__init__(Russia.id, Russia.name)


class Ukraine(Country):
    id = 1
    name = "Ukraine"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27

        class Infantry:
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            SNR_75V = vehicles.AirDefence.SNR_75V

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Hummer = vehicles.Unarmed.Hummer
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_27 = planes.Su_27
        MiG_29A = planes.MiG_29A
        MiG_29S = planes.MiG_29S
        Su_17M4 = planes.Su_17M4
        Tu_95MS = planes.Tu_95MS
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        MiG_25PD = planes.MiG_25PD
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        MiG_23MLD = planes.MiG_23MLD
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        MiG_27K = planes.MiG_27K
        Tu_22M3 = planes.Tu_22M3
        MiG_25RBT = planes.MiG_25RBT
        Yak_40 = planes.Yak_40
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_27,
        Plane.MiG_29A,
        Plane.MiG_29S,
        Plane.Su_17M4,
        Plane.Tu_95MS,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.MiG_25PD,
        Plane.An_26B,
        Plane.An_30M,
        Plane.MiG_23MLD,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.MiG_27K,
        Plane.Tu_22M3,
        Plane.MiG_25RBT,
        Plane.Yak_40,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        ALBATROS = ships.ALBATROS
        MOLNIYA = ships.MOLNIYA
        KILO = ships.KILO
        ZWEZDNY = ships.ZWEZDNY
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        REZKY = ships.REZKY

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Ukraine, self).__init__(Ukraine.id, Ukraine.name)


class USA(Country):
    id = 2
    name = "USA"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            M_109 = vehicles.Artillery.M_109
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            MLRS = vehicles.Artillery.MLRS
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class Infantry:
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_wwii_us = vehicles.Infantry.Soldier_wwii_us

        class AirDefence:
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            M6_Linebacker = vehicles.AirDefence.M6_Linebacker
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_str = vehicles.AirDefence.Patriot_str
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Vulcan = vehicles.AirDefence.Vulcan
            Bofors40 = vehicles.AirDefence.Bofors40
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            QF_37_AA = vehicles.AirDefence.QF_37_AA

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            M30_CC = vehicles.Unarmed.M30_CC
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD

        class Armor:
            AAV7 = vehicles.Armor.AAV7
            LAV_25 = vehicles.Armor.LAV_25
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            M_113 = vehicles.Armor.M_113
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            M_60 = vehicles.Armor.M_60
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M1126_Stryker_ICV = vehicles.Armor.M1126_Stryker_ICV
            M1128_Stryker_MGS = vehicles.Armor.M1128_Stryker_MGS
            M1134_Stryker_ATGM = vehicles.Armor.M1134_Stryker_ATGM
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            TPZ = vehicles.Armor.TPZ
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            M4_Sherman = vehicles.Armor.M4_Sherman
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            Tetrarch = vehicles.Armor.Tetrarch

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        A_10A = planes.A_10A
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        C_130 = planes.C_130
        C_17A = planes.C_17A
        E_2C = planes.E_2C
        E_3A = planes.E_3A
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        F_16A = planes.F_16A
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_A_18C = planes.F_A_18C
        KC_135 = planes.KC_135
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        RQ_1A_Predator = planes.RQ_1A_Predator
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        An_26B = planes.An_26B
        B_17G = planes.B_17G
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_50 = planes.F_16C_bl_50
        F_4E = planes.F_4E
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        F_A_18A = planes.F_A_18A
        FA_18C_hornet = planes.FA_18C_hornet
        KC135MPRS = planes.KC135MPRS
        L_39C = planes.L_39C
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        Christen_Eagle_II = planes.Christen_Eagle_II
        AV8BNA = planes.AV8BNA
        Hawk = planes.Hawk
        KC130 = planes.KC130
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        A_20G = planes.A_20G
        AJS37 = planes.AJS37
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.A_10A,
        Plane.B_1B,
        Plane.B_52H,
        Plane.C_130,
        Plane.C_17A,
        Plane.E_2C,
        Plane.E_3A,
        Plane.F_117A,
        Plane.F_14A,
        Plane.F_15C,
        Plane.F_15E,
        Plane.F_16A,
        Plane.F_16C_bl_52d,
        Plane.F_A_18C,
        Plane.KC_135,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.RQ_1A_Predator,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.An_26B,
        Plane.B_17G,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_50,
        Plane.F_4E,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.F_A_18A,
        Plane.FA_18C_hornet,
        Plane.KC135MPRS,
        Plane.L_39C,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.Christen_Eagle_II,
        Plane.AV8BNA,
        Plane.Hawk,
        Plane.KC130,
        Plane.A_10C_2,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.A_20G,
        Plane.AJS37,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        AH_1W = helicopters.AH_1W
        UH_60A = helicopters.UH_60A
        CH_47D = helicopters.CH_47D
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E
        OH_58D = helicopters.OH_58D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.AH_1W,
        Helicopter.UH_60A,
        Helicopter.CH_47D,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
        Helicopter.OH_58D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        VINSON = ships.VINSON
        PERRY = ships.PERRY
        TICONDEROG = ships.TICONDEROG
        Higgins_boat = ships.Higgins_boat
        LST_Mk2 = ships.LST_Mk2
        Stennis = ships.Stennis
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        LHA_Tarawa = ships.LHA_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
        CVN_71 = ships.CVN_71
        CVN_72 = ships.CVN_72
        CVN_73 = ships.CVN_73
        CVN_75 = ships.CVN_75
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        Forrestal = ships.Forrestal

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(USA, self).__init__(USA.id, USA.name)


class Turkey(Country):
    id = 3
    name = "Turkey"

    class Vehicle:

        class Artillery:
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M_109 = vehicles.Artillery.M_109
            T155_Firtina = vehicles.Artillery.T155_Firtina

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            M_113 = vehicles.Armor.M_113
            Cobra = vehicles.Armor.Cobra
            M_60 = vehicles.Armor.M_60
            AAV7 = vehicles.Armor.AAV7
            BTR_80 = vehicles.Armor.BTR_80
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A4_trs = vehicles.Armor.Leopard_2A4_trs

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_50 = planes.F_16C_bl_50
        F_4E = planes.F_4E
        C_130 = planes.C_130
        P_51D = planes.P_51D
        KC_135 = planes.KC_135
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        KC135MPRS = planes.KC135MPRS
        RQ_1A_Predator = planes.RQ_1A_Predator
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MQ_9_Reaper = planes.MQ_9_Reaper
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_50,
        Plane.F_4E,
        Plane.C_130,
        Plane.P_51D,
        Plane.KC_135,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.KC135MPRS,
        Plane.RQ_1A_Predator,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MQ_9_Reaper,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        Mi_8MT = helicopters.Mi_8MT
        AH_1W = helicopters.AH_1W
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.Mi_8MT,
        Helicopter.AH_1W,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Turkey, self).__init__(Turkey.id, Turkey.name)


class UK(Country):
    id = 4
    name = "UK"

    class Vehicle:

        class Artillery:
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class Infantry:
            Soldier_wwii_br_01 = vehicles.Infantry.Soldier_wwii_br_01

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            Bofors40 = vehicles.AirDefence.Bofors40
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            Willys_MB = vehicles.Unarmed.Willys_MB
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            MCV_80 = vehicles.Armor.MCV_80
            Challenger2 = vehicles.Armor.Challenger2
            TPZ = vehicles.Armor.TPZ
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            Tetrarch = vehicles.Armor.Tetrarch
            Daimler_AC = vehicles.Armor.Daimler_AC
            M4_Tractor = vehicles.Armor.M4_Tractor
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Tornado_GR4 = planes.Tornado_GR4
        C_130 = planes.C_130
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        AV8BNA = planes.AV8BNA
        Hawk = planes.Hawk
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        B_17G = planes.B_17G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Tornado_GR4,
        Plane.C_130,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.AV8BNA,
        Plane.Hawk,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.B_17G,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        LST_Mk2 = ships.LST_Mk2
        HandyWind = ships.HandyWind
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        Seawise_Giant = ships.Seawise_Giant
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Solex = "Solex"
        Image = "Image"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Solex,
            CallsignAWACS.Image
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UK, self).__init__(UK.id, UK.name)


class France(Country):
    id = 5
    name = "France"

    class Vehicle:

        class Artillery:
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Bofors40 = vehicles.AirDefence.Bofors40
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            Leclerc = vehicles.Armor.Leclerc
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            M10_GMC = vehicles.Armor.M10_GMC
            M4_Tractor = vehicles.Armor.M4_Tractor
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto
            M4_Sherman = vehicles.Armor.M4_Sherman
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            Tetrarch = vehicles.Armor.Tetrarch
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        C_130 = planes.C_130
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_2C = planes.E_2C
        E_3A = planes.E_3A
        KC_135 = planes.KC_135
        KC135MPRS = planes.KC135MPRS
        L_39C = planes.L_39C
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        M_2000C = planes.M_2000C
        KC130 = planes.KC130
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.C_130,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_2C,
        Plane.E_3A,
        Plane.KC_135,
        Plane.KC135MPRS,
        Plane.L_39C,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.M_2000C,
        Plane.KC130,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Cyrano = "Cyrano"
        Roxanne = "Roxanne"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Cyrano,
            CallsignAWACS.Roxanne
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(France, self).__init__(France.id, France.name)


class Germany(Country):
    id = 6
    name = "Germany"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Gepard = vehicles.AirDefence.Gepard
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            GAZ_66 = vehicles.Unarmed.GAZ_66
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ATZ_5 = vehicles.Unarmed.ATZ_5
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7

        class Armor:
            M_113 = vehicles.Armor.M_113
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Marder = vehicles.Armor.Marder
            TPZ = vehicles.Armor.TPZ
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

    class Plane:
        A_10C = planes.A_10C
        MiG_29G = planes.MiG_29G
        F_4E = planes.F_4E
        Tornado_IDS = planes.Tornado_IDS
        P_51D = planes.P_51D
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        Su_17M4 = planes.Su_17M4
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_29A = planes.MiG_29A
        C_47 = planes.C_47
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.MiG_29G,
        Plane.F_4E,
        Plane.Tornado_IDS,
        Plane.P_51D,
        Plane.An_26B,
        Plane.C_17A,
        Plane.E_3A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.Su_17M4,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_29A,
        Plane.C_47,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        La_Combattante_II = ships.La_Combattante_II
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Germany, self).__init__(Germany.id, Germany.name)


class USAFAggressors(Country):
    id = 7
    name = "USAF Aggressors"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            PLZ05 = vehicles.Artillery.PLZ05
            T155_Firtina = vehicles.Artillery.T155_Firtina

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4_GRG = vehicles.Infantry.Soldier_M4_GRG
            Soldier_wwii_us = vehicles.Infantry.Soldier_wwii_us
            Soldier_wwii_br_01 = vehicles.Infantry.Soldier_wwii_br_01

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SNR_75V = vehicles.AirDefence.SNR_75V
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            Gepard = vehicles.AirDefence.Gepard
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            M6_Linebacker = vehicles.AirDefence.M6_Linebacker

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ
            AA8 = vehicles.Unarmed.AA8
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Tigr_233036 = vehicles.Unarmed.Tigr_233036

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Tetrarch = vehicles.Armor.Tetrarch
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto
            T_90 = vehicles.Armor.T_90
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            AAV7 = vehicles.Armor.AAV7
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            Cobra = vehicles.Armor.Cobra
            LAV_25 = vehicles.Armor.LAV_25
            Merkava_Mk4 = vehicles.Armor.Merkava_Mk4
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Marder = vehicles.Armor.Marder
            Leclerc = vehicles.Armor.Leclerc
            ZBD04A = vehicles.Armor.ZBD04A
            ZTZ96B = vehicles.Armor.ZTZ96B
            Leopard_2A4_trs = vehicles.Armor.Leopard_2A4_trs
            Challenger2 = vehicles.Armor.Challenger2
            M1126_Stryker_ICV = vehicles.Armor.M1126_Stryker_ICV
            M1128_Stryker_MGS = vehicles.Armor.M1128_Stryker_MGS
            M1134_Stryker_ATGM = vehicles.Armor.M1134_Stryker_ATGM
            MCV_80 = vehicles.Armor.MCV_80

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        J_11A = planes.J_11A
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        Mirage_2000_5 = planes.Mirage_2000_5
        P_51D_30_NA = planes.P_51D_30_NA
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        KJ_2000 = planes.KJ_2000
        H_6J = planes.H_6J
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.J_11A,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.Mirage_2000_5,
        Plane.P_51D_30_NA,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.KJ_2000,
        Plane.H_6J,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        ALBATROS = ships.ALBATROS
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ELNYA = ships.ELNYA
        KUZNECOW = ships.KUZNECOW
        MOLNIYA = ships.MOLNIYA
        MOSCOW = ships.MOSCOW
        NEUSTRASH = ships.NEUSTRASH
        REZKY = ships.REZKY
        ZWEZDNY = ships.ZWEZDNY
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        PERRY = ships.PERRY
        PIOTR = ships.PIOTR
        CV_1143_5 = ships.CV_1143_5
        La_Combattante_II = ships.La_Combattante_II
        Type_052B = ships.Type_052B
        Type_052C = ships.Type_052C
        Type_054A = ships.Type_054A
        Type_071 = ships.Type_071
        Type_093 = ships.Type_093
        VINSON = ships.VINSON
        TICONDEROG = ships.TICONDEROG
        Stennis = ships.Stennis
        LHA_Tarawa = ships.LHA_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
        CVN_71 = ships.CVN_71
        CVN_72 = ships.CVN_72
        CVN_73 = ships.CVN_73
        CVN_75 = ships.CVN_75
        Forrestal = ships.Forrestal

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(USAFAggressors, self).__init__(USAFAggressors.id, USAFAggressors.name)


class Canada(Country):
    id = 8
    name = "Canada"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            M_113 = vehicles.Armor.M_113
            LAV_25 = vehicles.Armor.LAV_25
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            Daimler_AC = vehicles.Armor.Daimler_AC
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            M4_Sherman = vehicles.Armor.M4_Sherman
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        KC130 = planes.KC130
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.KC130,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Canada, self).__init__(Canada.id, Canada.name)


class Spain(Country):
    id = 9
    name = "Spain"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Bofors40 = vehicles.AirDefence.Bofors40
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit

        class Armor:
            M_113 = vehicles.Armor.M_113
            Leopard_2 = vehicles.Armor.Leopard_2
            M_60 = vehicles.Armor.M_60
            AAV7 = vehicles.Armor.AAV7
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A4 = vehicles.Armor.Leopard_2A4

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_4E = planes.F_4E
        F_86F_Sabre = planes.F_86F_Sabre
        MQ_9_Reaper = planes.MQ_9_Reaper
        AV8BNA = planes.AV8BNA
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        I_16 = planes.I_16
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_4E,
        Plane.F_86F_Sabre,
        Plane.MQ_9_Reaper,
        Plane.AV8BNA,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.I_16,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Spain, self).__init__(Spain.id, Spain.name)


class TheNetherlands(Country):
    id = 10
    name = "The Netherlands"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            Gepard = vehicles.AirDefence.Gepard
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard1A3 = vehicles.Armor.Leopard1A3
            TPZ = vehicles.Armor.TPZ
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            M4_Sherman = vehicles.Armor.M4_Sherman
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        MQ_9_Reaper = planes.MQ_9_Reaper
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.MQ_9_Reaper,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(TheNetherlands, self).__init__(TheNetherlands.id, TheNetherlands.name)


class Belgium(Country):
    id = 11
    name = "Belgium"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            Gepard = vehicles.AirDefence.Gepard
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            M_113 = vehicles.Armor.M_113
            Leopard1A3 = vehicles.Armor.Leopard1A3
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Daimler_AC = vehicles.Armor.Daimler_AC
            M4_Tractor = vehicles.Armor.M4_Tractor
            M4_Sherman = vehicles.Armor.M4_Sherman
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Belgium, self).__init__(Belgium.id, Belgium.name)


class Norway(Country):
    id = 12
    name = "Norway"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            M_113 = vehicles.Armor.M_113
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard1A3 = vehicles.Armor.Leopard1A3
            TPZ = vehicles.Armor.TPZ
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Norway, self).__init__(Norway.id, Norway.name)


class Denmark(Country):
    id = 13
    name = "Denmark"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            M_113 = vehicles.Armor.M_113
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A5 = vehicles.Armor.Leopard_2A5

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        B_17G = planes.B_17G
        C_17A = planes.C_17A
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.B_17G,
        Plane.C_17A,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Denmark, self).__init__(Denmark.id, Denmark.name)


class Israel(Country):
    id = 15
    name = "Israel"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Vulcan = vehicles.AirDefence.Vulcan
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            Bofors40 = vehicles.AirDefence.Bofors40
            QF_37_AA = vehicles.AirDefence.QF_37_AA

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            M_60 = vehicles.Armor.M_60
            T_55 = vehicles.Armor.T_55
            Merkava_Mk4 = vehicles.Armor.Merkava_Mk4
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            BRDM_2 = vehicles.Armor.BRDM_2
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Daimler_AC = vehicles.Armor.Daimler_AC

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        F_16C_bl_52d = planes.F_16C_bl_52d
        C_130 = planes.C_130
        F_4E = planes.F_4E
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        B_17G = planes.B_17G
        E_2C = planes.E_2C
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        MiG_21Bis = planes.MiG_21Bis
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        KC130 = planes.KC130
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_15C,
        Plane.F_15E,
        Plane.F_16C_bl_52d,
        Plane.C_130,
        Plane.F_4E,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.B_17G,
        Plane.E_2C,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.MiG_21Bis,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.KC130,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        UH_60A = helicopters.UH_60A
        AH_64D = helicopters.AH_64D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.UH_60A,
        Helicopter.AH_64D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Israel, self).__init__(Israel.id, Israel.name)


class Georgia(Country):
    id = 16
    name = "Georgia"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Msta = vehicles.Artillery.SAU_Msta
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class Infantry:
            Soldier_M4_GRG = vehicles.Infantry.Soldier_M4_GRG
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            M_818 = vehicles.Unarmed.M_818
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Hummer = vehicles.Unarmed.Hummer
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            ATZ_5 = vehicles.Unarmed.ATZ_5
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_80 = vehicles.Armor.BTR_80
            Cobra = vehicles.Armor.Cobra
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        An_26B = planes.An_26B
        Su_25T = planes.Su_25T
        L_39ZA = planes.L_39ZA
        Yak_40 = planes.Yak_40
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.An_26B,
        Plane.Su_25T,
        Plane.L_39ZA,
        Plane.Yak_40,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        ALBATROS = ships.ALBATROS
        MOLNIYA = ships.MOLNIYA
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ZWEZDNY = ships.ZWEZDNY
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Georgia, self).__init__(Georgia.id, Georgia.name)


class Insurgents(Country):
    id = 17
    name = "Insurgents"

    class Vehicle:

        class Artillery:
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            Grad_URAL = vehicles.Artillery.Grad_URAL
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class Infantry:
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ATZ_5 = vehicles.Unarmed.ATZ_5

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        P_51D = planes.P_51D
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.P_51D,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        MOLNIYA = ships.MOLNIYA
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ZWEZDNY = ships.ZWEZDNY

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Insurgents, self).__init__(Insurgents.id, Insurgents.name)


class Abkhazia(Country):
    id = 18
    name = "Abkhazia"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class Infantry:
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            ATZ_5 = vehicles.Unarmed.ATZ_5

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        Su_25 = planes.Su_25
        An_26B = planes.An_26B
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        TF_51D = planes.TF_51D
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.Su_25,
        Plane.An_26B,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.TF_51D,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        MOLNIYA = ships.MOLNIYA
        ZWEZDNY = ships.ZWEZDNY
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Abkhazia, self).__init__(Abkhazia.id, Abkhazia.name)


class SouthOssetia(Country):
    id = 19
    name = "South Ossetia"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class Infantry:
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            ATZ_5 = vehicles.Unarmed.ATZ_5

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(SouthOssetia, self).__init__(SouthOssetia.id, SouthOssetia.name)


class Italy(Country):
    id = 20
    name = "Italy"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit

        class Armor:
            M_113 = vehicles.Armor.M_113
            AAV7 = vehicles.Armor.AAV7
            Leopard1A3 = vehicles.Armor.Leopard1A3
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        Yak_40 = planes.Yak_40
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.Yak_40,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Italy, self).__init__(Italy.id, Italy.name)


class Australia(Country):
    id = 21
    name = "Australia"

    class Vehicle:

        class Artillery:
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            Leopard1A3 = vehicles.Armor.Leopard1A3
            LAV_25 = vehicles.Armor.LAV_25
            M_113 = vehicles.Armor.M_113
            Daimler_AC = vehicles.Armor.Daimler_AC
            M4_Sherman = vehicles.Armor.M4_Sherman
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        F_4E = planes.F_4E
        F_A_18A = planes.F_A_18A
        MQ_9_Reaper = planes.MQ_9_Reaper
        Hawk = planes.Hawk
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.F_4E,
        Plane.F_A_18A,
        Plane.MQ_9_Reaper,
        Plane.Hawk,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        SH_60B = helicopters.SH_60B
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.SH_60B,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Australia, self).__init__(Australia.id, Australia.name)


class Switzerland(Country):
    id = 22
    name = "Switzerland"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            Leopard_2 = vehicles.Armor.Leopard_2
            M_113 = vehicles.Armor.M_113
            Leopard_2A4 = vehicles.Armor.Leopard_2A4

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_A_18C = planes.F_A_18C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.F_A_18C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.MosquitoFBMkVI,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Switzerland, self).__init__(Switzerland.id, Switzerland.name)


class Austria(Country):
    id = 23
    name = "Austria"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M_60 = vehicles.Armor.M_60
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A4 = vehicles.Armor.Leopard_2A4

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Austria, self).__init__(Austria.id, Austria.name)


class Belarus(Country):
    id = 24
    name = "Belarus"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_72B3 = vehicles.Armor.T_72B3
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Locomotive = vehicles.Locomotive.Locomotive
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_76MD = planes.IL_76MD
        L_39C = planes.L_39C
        MiG_25PD = planes.MiG_25PD
        Su_30 = planes.Su_30
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_76MD,
        Plane.L_39C,
        Plane.MiG_25PD,
        Plane.Su_30,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Belarus, self).__init__(Belarus.id, Belarus.name)


class Bulgaria(Country):
    id = 25
    name = "Bulgaria"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            PT_76 = vehicles.Armor.PT_76
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Su_25 = planes.Su_25
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Su_25,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Bulgaria, self).__init__(Bulgaria.id, Bulgaria.name)


class CzechRepublic(Country):
    id = 26
    name = "Czech Republic"

    class Vehicle:

        class Artillery:
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            SNR_75V = vehicles.AirDefence.SNR_75V
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            M4_Sherman = vehicles.Armor.M4_Sherman
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        C_17A = planes.C_17A
        L_39C = planes.L_39C
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Su_25 = planes.Su_25
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.C_17A,
        Plane.L_39C,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Su_25,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CzechRepublic, self).__init__(CzechRepublic.id, CzechRepublic.name)


class China(Country):
    id = 27
    name = "China"

    class Vehicle:

        class Artillery:
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            PLZ05 = vehicles.Artillery.PLZ05

        class AirDefence:
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            ZIL_135 = vehicles.Unarmed.ZIL_135

        class Armor:
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            ZBD04A = vehicles.Armor.ZBD04A
            ZTZ96B = vehicles.Armor.ZTZ96B

        class MissilesSS:
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_27 = planes.Su_27
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        MiG_15bis = planes.MiG_15bis
        Su_30 = planes.Su_30
        I_16 = planes.I_16
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        MiG_19P = planes.MiG_19P
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        WingLoong_I = planes.WingLoong_I
        H_6J = planes.H_6J
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.Su_27,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.An_26B,
        Plane.An_30M,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.MiG_15bis,
        Plane.Su_30,
        Plane.I_16,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.MiG_19P,
        Plane.MosquitoFBMkVI,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.WingLoong_I,
        Plane.H_6J,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        KILO = ships.KILO
        Type_052B = ships.Type_052B
        Type_052C = ships.Type_052C
        Type_054A = ships.Type_054A
        HandyWind = ships.HandyWind
        Type_071 = ships.Type_071
        Type_093 = ships.Type_093
        Seawise_Giant = ships.Seawise_Giant

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(China, self).__init__(China.id, China.name)


class Croatia(Country):
    id = 28
    name = "Croatia"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            T_55 = vehicles.Armor.T_55
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_17A = planes.C_17A
        MiG_21Bis = planes.MiG_21Bis
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_17A,
        Plane.MiG_21Bis,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        OH_58D = helicopters.OH_58D
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.OH_58D,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Croatia, self).__init__(Croatia.id, Croatia.name)


class Egypt(Country):
    id = 29
    name = "Egypt"

    class Vehicle:

        class Artillery:
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            MLRS = vehicles.Artillery.MLRS

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            M_60 = vehicles.Armor.M_60
            T_55 = vehicles.Armor.T_55
            T_80UD = vehicles.Armor.T_80UD
            M10_GMC = vehicles.Armor.M10_GMC
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_16A = planes.F_16A
        F_4E = planes.F_4E
        MiG_15bis = planes.MiG_15bis
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        M_2000C = planes.M_2000C
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_16A,
        Plane.F_4E,
        Plane.MiG_15bis,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.M_2000C,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        MOLNIYA = ships.MOLNIYA
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Egypt, self).__init__(Egypt.id, Egypt.name)


class Finland(Country):
    id = 30
    name = "Finland"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            MLRS = vehicles.Artillery.MLRS
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            MTLB = vehicles.Armor.MTLB
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            PT_76 = vehicles.Armor.PT_76
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            Leopard_2 = vehicles.Armor.Leopard_2
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_A_18C = planes.F_A_18C
        MiG_21Bis = planes.MiG_21Bis
        Hawk = planes.Hawk
        I_16 = planes.I_16
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_A_18C,
        Plane.MiG_21Bis,
        Plane.Hawk,
        Plane.I_16,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Finland, self).__init__(Finland.id, Finland.name)


class Greece(Country):
    id = 31
    name = "Greece"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            Bofors40 = vehicles.AirDefence.Bofors40
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            Generator_5i57 = vehicles.AirDefence.Generator_5i57

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Trolley_bus = vehicles.Unarmed.Trolley_bus

        class Armor:
            BMP_1 = vehicles.Armor.BMP_1
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M_60 = vehicles.Armor.M_60
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            Leopard_2A4 = vehicles.Armor.Leopard_2A4

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_4E = planes.F_4E
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        Mirage_2000_5 = planes.Mirage_2000_5
        Yak_40 = planes.Yak_40
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        M_2000C = planes.M_2000C
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_4E,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.Mirage_2000_5,
        Plane.Yak_40,
        Plane.P_51D,
        Plane.C_17A,
        Plane.M_2000C,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        SH_60B = helicopters.SH_60B
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.SH_60B,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Greece, self).__init__(Greece.id, Greece.name)


class Hungary(Country):
    id = 32
    name = "Hungary"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Hungary, self).__init__(Hungary.id, Hungary.name)


class India(Country):
    id = 33
    name = "India"

    class Vehicle:

        class Artillery:
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            KrAZ6322 = vehicles.Unarmed.KrAZ6322

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_90 = vehicles.Armor.T_90
            Daimler_AC = vehicles.Armor.Daimler_AC
            PT_76 = vehicles.Armor.PT_76

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        A_50 = planes.A_50
        C_130 = planes.C_130
        C_17A = planes.C_17A
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Su_30 = planes.Su_30
        Tu_142 = planes.Tu_142
        MQ_9_Reaper = planes.MQ_9_Reaper
        M_2000C = planes.M_2000C
        Hawk = planes.Hawk
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.A_50,
        Plane.C_130,
        Plane.C_17A,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Su_30,
        Plane.Tu_142,
        Plane.MQ_9_Reaper,
        Plane.M_2000C,
        Plane.Hawk,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        MOLNIYA = ships.MOLNIYA
        KILO = ships.KILO
        MOLNIYA = ships.MOLNIYA
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(India, self).__init__(India.id, India.name)


class Iran(Country):
    id = 34
    name = "Iran"

    class Vehicle:

        class Artillery:
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            M_109 = vehicles.Artillery.M_109
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class Infantry:
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BTR_80 = vehicles.Armor.BTR_80
            T_72B = vehicles.Armor.T_72B
            T_55 = vehicles.Armor.T_55
            M_113 = vehicles.Armor.M_113
            M_60 = vehicles.Armor.M_60
            BMD_1 = vehicles.Armor.BMD_1
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        MiG_29A = planes.MiG_29A
        Su_25 = planes.Su_25
        Su_24M = planes.Su_24M
        IL_76MD = planes.IL_76MD
        MiG_21Bis = planes.MiG_21Bis
        A_50 = planes.A_50
        F_14A = planes.F_14A
        F_4E = planes.F_4E
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        Su_25T = planes.Su_25T
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.MiG_29A,
        Plane.Su_25,
        Plane.Su_24M,
        Plane.IL_76MD,
        Plane.MiG_21Bis,
        Plane.A_50,
        Plane.F_14A,
        Plane.F_4E,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.Su_25T,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_1W = helicopters.AH_1W
        OH_58D = helicopters.OH_58D
        Mi_8MT = helicopters.Mi_8MT
        CH_47D = helicopters.CH_47D
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_1W,
        Helicopter.OH_58D,
        Helicopter.Mi_8MT,
        Helicopter.CH_47D,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        KILO = ships.KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Iran, self).__init__(Iran.id, Iran.name)


class Iraq(Country):
    id = 35
    name = "Iraq"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            T_55 = vehicles.Armor.T_55
            T_90 = vehicles.Armor.T_90
            PT_76 = vehicles.Armor.PT_76
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        MiG_25PD = planes.MiG_25PD
        MiG_29A = planes.MiG_29A
        Su_24M = planes.Su_24M
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.MiG_25PD,
        Plane.MiG_29A,
        Plane.Su_24M,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_28N = helicopters.Mi_28N
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_28N,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Iraq, self).__init__(Iraq.id, Iraq.name)


class Japan(Country):
    id = 36
    name = "Japan"

    class Vehicle:

        class Artillery:
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_15C = planes.F_15C
        F_86F_Sabre = planes.F_86F_Sabre
        KC130 = planes.KC130
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_15C,
        Plane.F_86F_Sabre,
        Plane.KC130,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Japan, self).__init__(Japan.id, Japan.name)


class Kazakhstan(Country):
    id = 37
    name = "Kazakhstan"

    class Vehicle:

        class Artillery:
            SAU_Msta = vehicles.Artillery.SAU_Msta
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            Grad_URAL = vehicles.Artillery.Grad_URAL
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            Smerch = vehicles.Artillery.Smerch
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            SNR_75V = vehicles.AirDefence.SNR_75V

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            SKP_11 = vehicles.Unarmed.SKP_11
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Hummer = vehicles.Unarmed.Hummer
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            T_80UD = vehicles.Armor.T_80UD
            BMP_3 = vehicles.Armor.BMP_3
            BTR_D = vehicles.Armor.BTR_D
            MTLB = vehicles.Armor.MTLB
            T_72B = vehicles.Armor.T_72B
            T_55 = vehicles.Armor.T_55
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            Cobra = vehicles.Armor.Cobra
            BTR_82A = vehicles.Armor.BTR_82A

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Locomotive = vehicles.Locomotive.Locomotive
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        MiG_31 = planes.MiG_31
        Su_30 = planes.Su_30
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_76MD = planes.IL_76MD
        L_39C = planes.L_39C
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.MiG_31,
        Plane.Su_30,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_76MD,
        Plane.L_39C,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Kazakhstan, self).__init__(Kazakhstan.id, Kazakhstan.name)


class NorthKorea(Country):
    id = 38
    name = "North Korea"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            ZIL_135 = vehicles.Unarmed.ZIL_135

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BRDM_2 = vehicles.Armor.BRDM_2
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        MiG_29S = planes.MiG_29S
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.MiG_29S,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(NorthKorea, self).__init__(NorthKorea.id, NorthKorea.name)


class Pakistan(Country):
    id = 39
    name = "Pakistan"

    class Vehicle:

        class Artillery:
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375

        class Armor:
            M_113 = vehicles.Armor.M_113
            BRDM_2 = vehicles.Armor.BRDM_2
            T_55 = vehicles.Armor.T_55
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        IL_78M = planes.IL_78M
        WingLoong_I = planes.WingLoong_I
        JF_17 = planes.JF_17
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.IL_78M,
        Plane.WingLoong_I,
        Plane.JF_17,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Pakistan, self).__init__(Pakistan.id, Pakistan.name)


class Poland(Country):
    id = 40
    name = "Poland"

    class Vehicle:

        class Artillery:
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            Leopard_2 = vehicles.Armor.Leopard_2
            T_55 = vehicles.Armor.T_55
            Daimler_AC = vehicles.Armor.Daimler_AC
            PT_76 = vehicles.Armor.PT_76
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_50 = planes.F_16C_bl_50
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        An_26B = planes.An_26B
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_16C_bl_52d = planes.F_16C_bl_52d
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29G = planes.MiG_29G
        Yak_40 = planes.Yak_40
        I_16 = planes.I_16
        MiG_19P = planes.MiG_19P
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_50,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.An_26B,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_16C_bl_52d,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29G,
        Plane.Yak_40,
        Plane.I_16,
        Plane.MiG_19P,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY
        KILO = ships.KILO
        MOLNIYA = ships.MOLNIYA
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Poland, self).__init__(Poland.id, Poland.name)


class Romania(Country):
    id = 41
    name = "Romania"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Gepard = vehicles.AirDefence.Gepard
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_16A_MLU = planes.F_16A_MLU
        L_39ZA = planes.L_39ZA
        MiG_15bis = planes.MiG_15bis
        MiG_29A = planes.MiG_29A
        Yak_52 = planes.Yak_52
        I_16 = planes.I_16
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_16A_MLU,
        Plane.L_39ZA,
        Plane.MiG_15bis,
        Plane.MiG_29A,
        Plane.Yak_52,
        Plane.I_16,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        MOLNIYA = ships.MOLNIYA
        KILO = ships.KILO
        MOLNIYA = ships.MOLNIYA
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Romania, self).__init__(Romania.id, Romania.name)


class SaudiArabia(Country):
    id = 42
    name = "Saudi Arabia"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Vulcan = vehicles.AirDefence.Vulcan
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            TPZ = vehicles.Armor.TPZ
            Cobra = vehicles.Armor.Cobra
            LAV_25 = vehicles.Armor.LAV_25

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        Tornado_IDS = planes.Tornado_IDS
        C_130 = planes.C_130
        E_3A = planes.E_3A
        KC_135 = planes.KC_135
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        KC130 = planes.KC130
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.F_15C,
        Plane.F_15E,
        Plane.Tornado_IDS,
        Plane.C_130,
        Plane.E_3A,
        Plane.KC_135,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.KC130,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        UH_1H = helicopters.UH_1H
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        CH_47D = helicopters.CH_47D
        AH_64A = helicopters.AH_64A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.UH_1H,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.CH_47D,
        Helicopter.AH_64A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SaudiArabia, self).__init__(SaudiArabia.id, SaudiArabia.name)


class Serbia(Country):
    id = 43
    name = "Serbia"

    class Vehicle:

        class Artillery:
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Grad_URAL = vehicles.Artillery.Grad_URAL
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            SKP_11 = vehicles.Unarmed.SKP_11
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Hummer = vehicles.Unarmed.Hummer
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            Trolley_bus = vehicles.Unarmed.Trolley_bus

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            MTLB = vehicles.Armor.MTLB
            T_72B = vehicles.Armor.T_72B
            T_55 = vehicles.Armor.T_55
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        MiG_29A = planes.MiG_29A
        MiG_21Bis = planes.MiG_21Bis
        An_26B = planes.An_26B
        MiG_29S = planes.MiG_29S
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        WingLoong_I = planes.WingLoong_I
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.MiG_29A,
        Plane.MiG_21Bis,
        Plane.An_26B,
        Plane.MiG_29S,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.WingLoong_I,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Serbia, self).__init__(Serbia.id, Serbia.name)


class Slovakia(Country):
    id = 44
    name = "Slovakia"

    class Vehicle:

        class Artillery:
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class AirDefence:
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        L_39C = planes.L_39C
        MiG_29A = planes.MiG_29A
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.L_39C,
        Plane.MiG_29A,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Slovakia, self).__init__(Slovakia.id, Slovakia.name)


class SouthKorea(Country):
    id = 45
    name = "South Korea"

    class Vehicle:

        class Artillery:
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            AAV7 = vehicles.Armor.AAV7
            M_113 = vehicles.Armor.M_113
            BMP_3 = vehicles.Armor.BMP_3
            T_80UD = vehicles.Armor.T_80UD
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_130 = planes.C_130
        F_15E = planes.F_15E
        F_4E = planes.F_4E
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_130,
        Plane.F_15E,
        Plane.F_4E,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SouthKorea, self).__init__(SouthKorea.id, SouthKorea.name)


class Sweden(Country):
    id = 46
    name = "Sweden"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            BMP_1 = vehicles.Armor.BMP_1
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            Leopard_2A5 = vehicles.Armor.Leopard_2A5

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        B_17G = planes.B_17G
        C_130 = planes.C_130
        AJS37 = planes.AJS37
        KC130 = planes.KC130
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.B_17G,
        Plane.C_130,
        Plane.AJS37,
        Plane.KC130,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Sweden, self).__init__(Sweden.id, Sweden.name)


class Syria(Country):
    id = 47
    name = "Syria"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class Infantry:
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_AK = vehicles.Infantry.Soldier_AK

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_90 = vehicles.Armor.T_90
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            PT_76 = vehicles.Armor.PT_76
            T_72B = vehicles.Armor.T_72B

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_29A = planes.MiG_29A
        Su_24M = planes.Su_24M
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_29A,
        Plane.Su_24M,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Syria, self).__init__(Syria.id, Syria.name)


class Yemen(Country):
    id = 48
    name = "Yemen"

    class Vehicle:

        class Artillery:
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            ZIL_135 = vehicles.Unarmed.ZIL_135

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        L_39C = planes.L_39C
        MiG_29S = planes.MiG_29S
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.L_39C,
        Plane.MiG_29S,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        MOLNIYA = ships.MOLNIYA

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Yemen, self).__init__(Yemen.id, Yemen.name)


class Vietnam(Country):
    id = 49
    name = "Vietnam"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_90 = vehicles.Armor.T_90
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        Su_17M4 = planes.Su_17M4
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.Su_17M4,
        Plane.Su_27,
        Plane.Su_30,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        MOLNIYA = ships.MOLNIYA
        HandyWind = ships.HandyWind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Vietnam, self).__init__(Vietnam.id, Vietnam.name)


class Venezuela(Country):
    id = 50
    name = "Venezuela"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            Smerch = vehicles.Artillery.Smerch
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch_HE = vehicles.Artillery.Smerch_HE
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            Generator_5i57 = vehicles.AirDefence.Generator_5i57

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            TPZ = vehicles.Armor.TPZ
            T_72B = vehicles.Armor.T_72B
            BMP_3 = vehicles.Armor.BMP_3

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        Su_30 = planes.Su_30
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.Su_30,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Venezuela, self).__init__(Venezuela.id, Venezuela.name)


class Tunisia(Country):
    id = 51
    name = "Tunisia"

    class Vehicle:

        class AirDefence:
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_60 = vehicles.Armor.M_60

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Tunisia, self).__init__(Tunisia.id, Tunisia.name)


class Thailand(Country):
    id = 52
    name = "Thailand"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322

        class Armor:
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_60 = vehicles.Armor.M_60
            AAV7 = vehicles.Armor.AAV7

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        L_39ZA = planes.L_39ZA
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.L_39ZA,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Thailand, self).__init__(Thailand.id, Thailand.name)


class Sudan(Country):
    id = 53
    name = "Sudan"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        MiG_29S = planes.MiG_29S
        Su_24M = planes.Su_24M
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.MiG_29S,
        Plane.Su_24M,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Sudan, self).__init__(Sudan.id, Sudan.name)


class Philippines(Country):
    id = 54
    name = "Philippines"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Philippines, self).__init__(Philippines.id, Philippines.name)


class Morocco(Country):
    id = 55
    name = "Morocco"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            Vulcan = vehicles.AirDefence.Vulcan
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            M_113 = vehicles.Armor.M_113
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            T_72B = vehicles.Armor.T_72B
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Morocco, self).__init__(Morocco.id, Morocco.name)


class Mexico(Country):
    id = 56
    name = "Mexico"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Mexico, self).__init__(Mexico.id, Mexico.name)


class Malaysia(Country):
    id = 57
    name = "Malaysia"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            Daimler_AC = vehicles.Armor.Daimler_AC

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Su_30 = planes.Su_30
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Su_30,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Malaysia, self).__init__(Malaysia.id, Malaysia.name)


class Libya(Country):
    id = 58
    name = "Libya"

    class Vehicle:

        class Artillery:
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        IL_78M = planes.IL_78M
        MiG_21Bis = planes.MiG_21Bis
        Su_24M = planes.Su_24M
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.IL_78M,
        Plane.MiG_21Bis,
        Plane.Su_24M,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Libya, self).__init__(Libya.id, Libya.name)


class Jordan(Country):
    id = 59
    name = "Jordan"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Gepard = vehicles.AirDefence.Gepard
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            M_113 = vehicles.Armor.M_113
            Marder = vehicles.Armor.Marder
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60
            BMP_2 = vehicles.Armor.BMP_2
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_1W = helicopters.AH_1W
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_1W,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Jordan, self).__init__(Jordan.id, Jordan.name)


class Indonesia(Country):
    id = 60
    name = "Indonesia"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            M_109 = vehicles.Artillery.M_109

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Bofors40 = vehicles.AirDefence.Bofors40
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Tigr_233036 = vehicles.Unarmed.Tigr_233036

        class Armor:
            AAV7 = vehicles.Armor.AAV7
            BTR_80 = vehicles.Armor.BTR_80
            M_113 = vehicles.Armor.M_113
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            Marder = vehicles.Armor.Marder
            PT_76 = vehicles.Armor.PT_76
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            Cobra = vehicles.Armor.Cobra
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        Hawk = planes.Hawk
        KC130 = planes.KC130
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_52d,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Su_27,
        Plane.Su_30,
        Plane.Hawk,
        Plane.KC130,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D = helicopters.AH_64D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Indonesia, self).__init__(Indonesia.id, Indonesia.name)


class Honduras(Country):
    id = 61
    name = "Honduras"

    class Vehicle:

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Honduras, self).__init__(Honduras.id, Honduras.name)


class Ethiopia(Country):
    id = 62
    name = "Ethiopia"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            BRDM_2 = vehicles.Armor.BRDM_2
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Yak_40 = planes.Yak_40
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Yak_40,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Ethiopia, self).__init__(Ethiopia.id, Ethiopia.name)


class Chile(Country):
    id = 63
    name = "Chile"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Vulcan = vehicles.AirDefence.Vulcan
            Bofors40 = vehicles.AirDefence.Bofors40
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            Gepard = vehicles.AirDefence.Gepard
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            Marder = vehicles.Armor.Marder
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Leopard_2A4 = vehicles.Armor.Leopard_2A4

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        KC_135 = planes.KC_135
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        KC135MPRS = planes.KC135MPRS
        C_130 = planes.C_130
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.KC_135,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.KC135MPRS,
        Plane.C_130,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        La_Combattante_II = ships.La_Combattante_II

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Chile, self).__init__(Chile.id, Chile.name)


class Brazil(Country):
    id = 64
    name = "Brazil"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            Gepard = vehicles.AirDefence.Gepard

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            M_113 = vehicles.Armor.M_113
            AAV7 = vehicles.Armor.AAV7
            M_60 = vehicles.Armor.M_60
            Leopard1A3 = vehicles.Armor.Leopard1A3
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        B_17G = planes.B_17G
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        M_2000C = planes.M_2000C
        KC130 = planes.KC130
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.B_17G,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.M_2000C,
        Plane.KC130,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Brazil, self).__init__(Brazil.id, Brazil.name)


class Bahrain(Country):
    id = 65
    name = "Bahrain"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            Cobra = vehicles.Armor.Cobra
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        PERRY = ships.PERRY

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Bahrain, self).__init__(Bahrain.id, Bahrain.name)


class ThirdReich(Country):
    id = 66
    name = "Third Reich"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(ThirdReich, self).__init__(ThirdReich.id, ThirdReich.name)


class Yugoslavia(Country):
    id = 67
    name = "Yugoslavia"

    class Vehicle:

        class Artillery:
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class AirDefence:
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Bofors40 = vehicles.AirDefence.Bofors40
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_375 = vehicles.Unarmed.Ural_375
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZIL_135 = vehicles.Unarmed.ZIL_135
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            T_55 = vehicles.Armor.T_55
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Centaur_IV = vehicles.Armor.Centaur_IV
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            Tetrarch = vehicles.Armor.Tetrarch
            M10_GMC = vehicles.Armor.M10_GMC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Yak_40 = planes.Yak_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Yak_40,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Yugoslavia, self).__init__(Yugoslavia.id, Yugoslavia.name)


class USSR(Country):
    id = 68
    name = "USSR"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SNR_75V = vehicles.AirDefence.SNR_75V
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ
            AA8 = vehicles.Unarmed.AA8
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC

        class Armor:
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Tetrarch = vehicles.Armor.Tetrarch
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_cargo = vehicles.Carriage.Coach_cargo
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

    class Plane:
        A_10C = planes.A_10C
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        I_16 = planes.I_16
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_19P = planes.MiG_19P
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        M_2000C = planes.M_2000C
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.I_16,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_19P,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.M_2000C,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ALBATROS = ships.ALBATROS
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ELNYA = ships.ELNYA
        KUZNECOW = ships.KUZNECOW
        MOLNIYA = ships.MOLNIYA
        MOSCOW = ships.MOSCOW
        NEUSTRASH = ships.NEUSTRASH
        REZKY = ships.REZKY
        ZWEZDNY = ships.ZWEZDNY
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(USSR, self).__init__(USSR.id, USSR.name)


class ItalianSocialRepublic(Country):
    id = 69
    name = "Italian Social Republic"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(ItalianSocialRepublic, self).__init__(ItalianSocialRepublic.id, ItalianSocialRepublic.name)


class Algeria(Country):
    id = 70
    name = "Algeria"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            GAZ_66 = vehicles.Unarmed.GAZ_66
            Hummer = vehicles.Unarmed.Hummer
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            M_818 = vehicles.Unarmed.M_818
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            SKP_11 = vehicles.Unarmed.SKP_11
            Tigr_233036 = vehicles.Unarmed.Tigr_233036
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_90 = vehicles.Armor.T_90
            TPZ = vehicles.Armor.TPZ

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        MiG_25PD = planes.MiG_25PD
        MiG_29S = planes.MiG_29S
        MiG_27K = planes.MiG_27K
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        L_39ZA = planes.L_39ZA
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        C_130 = planes.C_130
        Yak_40 = planes.Yak_40
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.MiG_25PD,
        Plane.MiG_29S,
        Plane.MiG_27K,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Su_30,
        Plane.L_39ZA,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.C_130,
        Plane.Yak_40,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_28N = helicopters.Mi_28N
        Ka_27 = helicopters.Ka_27
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_28N,
        Helicopter.Ka_27,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        ALBATROS = ships.ALBATROS
        MOLNIYA = ships.MOLNIYA
        KILO = ships.KILO
        ZWEZDNY = ships.ZWEZDNY
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        REZKY = ships.REZKY

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Algeria, self).__init__(Algeria.id, Algeria.name)


class Kuwait(Country):
    id = 71
    name = "Kuwait"

    class Vehicle:

        class Artillery:
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class AirDefence:
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Hummer = vehicles.Unarmed.Hummer
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            MCV_80 = vehicles.Armor.MCV_80
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_A_18C = planes.F_A_18C
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_A_18C,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D = helicopters.AH_64D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Kuwait, self).__init__(Kuwait.id, Kuwait.name)


class Qatar(Country):
    id = 72
    name = "Qatar"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Hummer = vehicles.Unarmed.Hummer

        class Armor:
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            Daimler_AC = vehicles.Armor.Daimler_AC
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_17A = planes.C_17A
        Mirage_2000_5 = planes.Mirage_2000_5
        M_2000C = planes.M_2000C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_17A,
        Plane.Mirage_2000_5,
        Plane.M_2000C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Qatar, self).__init__(Qatar.id, Qatar.name)


class Oman(Country):
    id = 73
    name = "Oman"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            Grad_URAL = vehicles.Artillery.Grad_URAL

        class AirDefence:
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Vulcan = vehicles.AirDefence.Vulcan
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Bofors40 = vehicles.AirDefence.Bofors40
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            Challenger2 = vehicles.Armor.Challenger2
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            BTR_80 = vehicles.Armor.BTR_80
            M_60 = vehicles.Armor.M_60

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16C_bl_50 = planes.F_16C_bl_50
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16C_bl_52d,
        Plane.F_16C_bl_50,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Oman, self).__init__(Oman.id, Oman.name)


class UnitedArabEmirates(Country):
    id = 74
    name = "United Arab Emirates"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109
            Grad_URAL = vehicles.Artillery.Grad_URAL
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE

        class AirDefence:
            Patriot_str = vehicles.AirDefence.Patriot_str
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Bofors40 = vehicles.AirDefence.Bofors40
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            BMP_3 = vehicles.Armor.BMP_3
            TPZ = vehicles.Armor.TPZ
            Leclerc = vehicles.Armor.Leclerc
            Cobra = vehicles.Armor.Cobra

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_52d = planes.F_16C_bl_52d
        C_130 = planes.C_130
        C_17A = planes.C_17A
        M_2000C = planes.M_2000C
        Hawk = planes.Hawk
        WingLoong_I = planes.WingLoong_I
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_52d,
        Plane.C_130,
        Plane.C_17A,
        Plane.M_2000C,
        Plane.Hawk,
        Plane.WingLoong_I,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D = helicopters.AH_64D
        UH_60A = helicopters.UH_60A
        CH_47D = helicopters.CH_47D
        AH_64A = helicopters.AH_64A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D,
        Helicopter.UH_60A,
        Helicopter.CH_47D,
        Helicopter.AH_64A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UnitedArabEmirates, self).__init__(UnitedArabEmirates.id, UnitedArabEmirates.name)


class SouthAfrica(Country):
    id = 75
    name = "South Africa"

    class Vehicle:

        class AirDefence:
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            Bofors40 = vehicles.AirDefence.Bofors40

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        C_130 = planes.C_130
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.C_130,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.MosquitoFBMkVI,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SouthAfrica, self).__init__(SouthAfrica.id, SouthAfrica.name)


class Cuba(Country):
    id = 76
    name = "Cuba"

    class Vehicle:

        class Artillery:
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            Grad_URAL = vehicles.Artillery.Grad_URAL
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            SKP_11 = vehicles.Unarmed.SKP_11
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            ZIL_135 = vehicles.Unarmed.ZIL_135

        class Armor:
            BTR_80 = vehicles.Armor.BTR_80
            BMP_1 = vehicles.Armor.BMP_1
            BRDM_2 = vehicles.Armor.BRDM_2
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            BMD_1 = vehicles.Armor.BMD_1
            PT_76 = vehicles.Armor.PT_76

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        MiG_23MLD = planes.MiG_23MLD
        MiG_29A = planes.MiG_29A
        MiG_21Bis = planes.MiG_21Bis
        An_26B = planes.An_26B
        Yak_40 = planes.Yak_40
        L_39ZA = planes.L_39ZA
        IL_76MD = planes.IL_76MD
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_23MLD = planes.MiG_23MLD
        MiG_23MLD = planes.MiG_23MLD
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.MiG_23MLD,
        Plane.MiG_29A,
        Plane.MiG_21Bis,
        Plane.An_26B,
        Plane.Yak_40,
        Plane.L_39ZA,
        Plane.IL_76MD,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_23MLD,
        Plane.MiG_23MLD,
        Plane.MiG_23MLD,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        ELNYA = ships.ELNYA
        ALBATROS = ships.ALBATROS
        MOLNIYA = ships.MOLNIYA
        ZWEZDNY = ships.ZWEZDNY
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Cuba, self).__init__(Cuba.id, Cuba.name)


class Portugal(Country):
    id = 77
    name = "Portugal"

    class Vehicle:

        class Artillery:
            M_109 = vehicles.Artillery.M_109

        class AirDefence:
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Vulcan = vehicles.AirDefence.Vulcan
            Bofors40 = vehicles.AirDefence.Bofors40
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            Leopard_2 = vehicles.Armor.Leopard_2
            M_60 = vehicles.Armor.M_60
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M4_Tractor = vehicles.Armor.M4_Tractor

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        F_86F_Sabre = planes.F_86F_Sabre
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        B_17G = planes.B_17G
        C_17A = planes.C_17A
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.F_86F_Sabre,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.B_17G,
        Plane.C_17A,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Portugal, self).__init__(Portugal.id, Portugal.name)


class GDR(Country):
    id = 78
    name = "GDR"

    class Vehicle:

        class Artillery:
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            SNR_75V = vehicles.AirDefence.SNR_75V
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_66 = vehicles.Unarmed.GAZ_66
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz

        class Armor:
            MTLB = vehicles.Armor.MTLB
            BRDM_2 = vehicles.Armor.BRDM_2
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class MissilesSS:
            Scud_B = vehicles.MissilesSS.Scud_B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(GDR, self).__init__(GDR.id, GDR.name)


class Lebanon(Country):
    id = 79
    name = "Lebanon"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            M_109 = vehicles.Artillery.M_109

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4 = vehicles.Infantry.Soldier_M4

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            Hummer = vehicles.Unarmed.Hummer
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            M_818 = vehicles.Unarmed.M_818

        class Armor:
            TPZ = vehicles.Armor.TPZ
            M_113 = vehicles.Armor.M_113
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            M_60 = vehicles.Armor.M_60
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            T_55 = vehicles.Armor.T_55
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        M_2000C = planes.M_2000C
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.M_2000C,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Lebanon, self).__init__(Lebanon.id, Lebanon.name)


class CombinedJointTaskForcesBlue(Country):
    id = 80
    name = "Combined Joint Task Forces Blue"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            PLZ05 = vehicles.Artillery.PLZ05
            T155_Firtina = vehicles.Artillery.T155_Firtina

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4_GRG = vehicles.Infantry.Soldier_M4_GRG
            Soldier_wwii_us = vehicles.Infantry.Soldier_wwii_us
            Soldier_wwii_br_01 = vehicles.Infantry.Soldier_wwii_br_01

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SNR_75V = vehicles.AirDefence.SNR_75V
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            Gepard = vehicles.AirDefence.Gepard
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            M6_Linebacker = vehicles.AirDefence.M6_Linebacker

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ
            AA8 = vehicles.Unarmed.AA8
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Tigr_233036 = vehicles.Unarmed.Tigr_233036

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Tetrarch = vehicles.Armor.Tetrarch
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto
            T_90 = vehicles.Armor.T_90
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            AAV7 = vehicles.Armor.AAV7
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            Cobra = vehicles.Armor.Cobra
            LAV_25 = vehicles.Armor.LAV_25
            Merkava_Mk4 = vehicles.Armor.Merkava_Mk4
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Marder = vehicles.Armor.Marder
            Leclerc = vehicles.Armor.Leclerc
            ZBD04A = vehicles.Armor.ZBD04A
            ZTZ96B = vehicles.Armor.ZTZ96B
            Leopard_2A4_trs = vehicles.Armor.Leopard_2A4_trs
            Challenger2 = vehicles.Armor.Challenger2
            M1126_Stryker_ICV = vehicles.Armor.M1126_Stryker_ICV
            M1128_Stryker_MGS = vehicles.Armor.M1128_Stryker_MGS
            M1134_Stryker_ATGM = vehicles.Armor.M1134_Stryker_ATGM
            MCV_80 = vehicles.Armor.MCV_80

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        Mirage_2000_5 = planes.Mirage_2000_5
        P_51D_30_NA = planes.P_51D_30_NA
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        H_6J = planes.H_6J
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.Mirage_2000_5,
        Plane.P_51D_30_NA,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.H_6J,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        ALBATROS = ships.ALBATROS
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ELNYA = ships.ELNYA
        KUZNECOW = ships.KUZNECOW
        MOLNIYA = ships.MOLNIYA
        MOSCOW = ships.MOSCOW
        NEUSTRASH = ships.NEUSTRASH
        REZKY = ships.REZKY
        ZWEZDNY = ships.ZWEZDNY
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        PERRY = ships.PERRY
        PIOTR = ships.PIOTR
        CV_1143_5 = ships.CV_1143_5
        La_Combattante_II = ships.La_Combattante_II
        Type_052B = ships.Type_052B
        Type_052C = ships.Type_052C
        Type_054A = ships.Type_054A
        Type_071 = ships.Type_071
        Type_093 = ships.Type_093
        VINSON = ships.VINSON
        TICONDEROG = ships.TICONDEROG
        Stennis = ships.Stennis
        LHA_Tarawa = ships.LHA_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
        CVN_71 = ships.CVN_71
        CVN_72 = ships.CVN_72
        CVN_73 = ships.CVN_73
        CVN_75 = ships.CVN_75
        Forrestal = ships.Forrestal

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CombinedJointTaskForcesBlue, self).__init__(CombinedJointTaskForcesBlue.id, CombinedJointTaskForcesBlue.name)


class CombinedJointTaskForcesRed(Country):
    id = 81
    name = "Combined Joint Task Forces Red"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            PLZ05 = vehicles.Artillery.PLZ05
            T155_Firtina = vehicles.Artillery.T155_Firtina

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4_GRG = vehicles.Infantry.Soldier_M4_GRG
            Soldier_wwii_us = vehicles.Infantry.Soldier_wwii_us
            Soldier_wwii_br_01 = vehicles.Infantry.Soldier_wwii_br_01

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SNR_75V = vehicles.AirDefence.SNR_75V
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            Gepard = vehicles.AirDefence.Gepard
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            M6_Linebacker = vehicles.AirDefence.M6_Linebacker

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ
            AA8 = vehicles.Unarmed.AA8
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Tigr_233036 = vehicles.Unarmed.Tigr_233036

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Tetrarch = vehicles.Armor.Tetrarch
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto
            T_90 = vehicles.Armor.T_90
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            AAV7 = vehicles.Armor.AAV7
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            Cobra = vehicles.Armor.Cobra
            LAV_25 = vehicles.Armor.LAV_25
            Merkava_Mk4 = vehicles.Armor.Merkava_Mk4
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Marder = vehicles.Armor.Marder
            Leclerc = vehicles.Armor.Leclerc
            ZBD04A = vehicles.Armor.ZBD04A
            ZTZ96B = vehicles.Armor.ZTZ96B
            Leopard_2A4_trs = vehicles.Armor.Leopard_2A4_trs
            Challenger2 = vehicles.Armor.Challenger2
            M1126_Stryker_ICV = vehicles.Armor.M1126_Stryker_ICV
            M1128_Stryker_MGS = vehicles.Armor.M1128_Stryker_MGS
            M1134_Stryker_ATGM = vehicles.Armor.M1134_Stryker_ATGM
            MCV_80 = vehicles.Armor.MCV_80

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        Mirage_2000_5 = planes.Mirage_2000_5
        P_51D_30_NA = planes.P_51D_30_NA
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        H_6J = planes.H_6J
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.Mirage_2000_5,
        Plane.P_51D_30_NA,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.H_6J,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        ALBATROS = ships.ALBATROS
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ELNYA = ships.ELNYA
        KUZNECOW = ships.KUZNECOW
        MOLNIYA = ships.MOLNIYA
        MOSCOW = ships.MOSCOW
        NEUSTRASH = ships.NEUSTRASH
        REZKY = ships.REZKY
        ZWEZDNY = ships.ZWEZDNY
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        PERRY = ships.PERRY
        PIOTR = ships.PIOTR
        CV_1143_5 = ships.CV_1143_5
        La_Combattante_II = ships.La_Combattante_II
        Type_052B = ships.Type_052B
        Type_052C = ships.Type_052C
        Type_054A = ships.Type_054A
        Type_071 = ships.Type_071
        Type_093 = ships.Type_093
        VINSON = ships.VINSON
        TICONDEROG = ships.TICONDEROG
        Stennis = ships.Stennis
        LHA_Tarawa = ships.LHA_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
        CVN_71 = ships.CVN_71
        CVN_72 = ships.CVN_72
        CVN_73 = ships.CVN_73
        CVN_75 = ships.CVN_75
        Forrestal = ships.Forrestal

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CombinedJointTaskForcesRed, self).__init__(CombinedJointTaskForcesRed.id, CombinedJointTaskForcesRed.name)


class UnitedNationsPeacekeepers(Country):
    id = 82
    name = "United Nations Peacekeepers"

    class Vehicle:

        class Artillery:
            Wespe124 = vehicles.Artillery.Wespe124
            Pak40 = vehicles.Artillery.Pak40
            LeFH_18_40_105 = vehicles.Artillery.LeFH_18_40_105
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            Grad_FDDM = vehicles.Artillery.Grad_FDDM
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SAU_2_C9 = vehicles.Artillery.SAU_2_C9
            SAU_Akatsia = vehicles.Artillery.SAU_Akatsia
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika
            SAU_Msta = vehicles.Artillery.SAU_Msta
            Smerch = vehicles.Artillery.Smerch
            Smerch_HE = vehicles.Artillery.Smerch_HE
            Uragan_BM_27 = vehicles.Artillery.Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            M2A1_105 = vehicles.Artillery.M2A1_105
            M_109 = vehicles.Artillery.M_109
            MLRS = vehicles.Artillery.MLRS
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            PLZ05 = vehicles.Artillery.PLZ05
            T155_Firtina = vehicles.Artillery.T155_Firtina

        class Infantry:
            Soldier_mauser98 = vehicles.Infantry.Soldier_mauser98
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3
            Paratrooper_AKS_74 = vehicles.Infantry.Paratrooper_AKS_74
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_AK_Ins = vehicles.Infantry.Infantry_AK_Ins
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M4 = vehicles.Infantry.Soldier_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4_GRG = vehicles.Infantry.Soldier_M4_GRG
            Soldier_wwii_us = vehicles.Infantry.Soldier_wwii_us
            Soldier_wwii_br_01 = vehicles.Infantry.Soldier_wwii_br_01

        class AirDefence:
            Flak18 = vehicles.AirDefence.Flak18
            Flak30 = vehicles.AirDefence.Flak30
            Flak36 = vehicles.AirDefence.Flak36
            Flak37 = vehicles.AirDefence.Flak37
            Flak38 = vehicles.AirDefence.Flak38
            KDO_Mod40 = vehicles.AirDefence.KDO_Mod40
            Flakscheinwerfer_37 = vehicles.AirDefence.Flakscheinwerfer_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            Flak41 = vehicles.AirDefence.Flak41
            FuMG_401 = vehicles.AirDefence.FuMG_401
            FuSe_65 = vehicles.AirDefence.FuSe_65
            _1L13_EWR = vehicles.AirDefence._1L13_EWR
            _2S6_Tunguska = vehicles.AirDefence._2S6_Tunguska
            _55G6_EWR = vehicles.AirDefence._55G6_EWR
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            Dog_Ear_radar = vehicles.AirDefence.Dog_Ear_radar
            Kub_1S91_str = vehicles.AirDefence.Kub_1S91_str
            Kub_2P25_ln = vehicles.AirDefence.Kub_2P25_ln
            Osa_9A33_ln = vehicles.AirDefence.Osa_9A33_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            S_75M_Volhov = vehicles.AirDefence.S_75M_Volhov
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            SA_18_Igla_comm = vehicles.AirDefence.SA_18_Igla_comm
            SA_18_Igla_manpad = vehicles.AirDefence.SA_18_Igla_manpad
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            SNR_75V = vehicles.AirDefence.SNR_75V
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            Strela_10M3 = vehicles.AirDefence.Strela_10M3
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Bofors40 = vehicles.AirDefence.Bofors40
            S_200_Launcher = vehicles.AirDefence.S_200_Launcher
            RPC_5N62V = vehicles.AirDefence.RPC_5N62V
            S_60_Type59_Artillery = vehicles.AirDefence.S_60_Type59_Artillery
            Generator_5i57 = vehicles.AirDefence.Generator_5i57
            RLS_19J6 = vehicles.AirDefence.RLS_19J6
            ZSU_57_2 = vehicles.AirDefence.ZSU_57_2
            QF_37_AA = vehicles.AirDefence.QF_37_AA
            M45_Quadmount = vehicles.AirDefence.M45_Quadmount
            M1_37mm = vehicles.AirDefence.M1_37mm
            Vulcan = vehicles.AirDefence.Vulcan
            Hawk_tr = vehicles.AirDefence.Hawk_tr
            Hawk_sr = vehicles.AirDefence.Hawk_sr
            Hawk_ln = vehicles.AirDefence.Hawk_ln
            Hawk_cwar = vehicles.AirDefence.Hawk_cwar
            Hawk_pcp = vehicles.AirDefence.Hawk_pcp
            M48_Chaparral = vehicles.AirDefence.M48_Chaparral
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            ZU_23_Closed_Insurgent = vehicles.AirDefence.ZU_23_Closed_Insurgent
            ZU_23_Insurgent = vehicles.AirDefence.ZU_23_Insurgent
            Ural_375_ZU_23_Insurgent = vehicles.AirDefence.Ural_375_ZU_23_Insurgent
            M1097_Avenger = vehicles.AirDefence.M1097_Avenger
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger
            Stinger_comm = vehicles.AirDefence.Stinger_comm
            Stinger_comm_dsr = vehicles.AirDefence.Stinger_comm_dsr
            Rapier_fsa_launcher = vehicles.AirDefence.Rapier_fsa_launcher
            Rapier_fsa_optical_tracker_unit = vehicles.AirDefence.Rapier_fsa_optical_tracker_unit
            Rapier_fsa_blindfire_radar = vehicles.AirDefence.Rapier_fsa_blindfire_radar
            Patriot_AMG = vehicles.AirDefence.Patriot_AMG
            Patriot_ECS = vehicles.AirDefence.Patriot_ECS
            Patriot_ln = vehicles.AirDefence.Patriot_ln
            Patriot_EPP = vehicles.AirDefence.Patriot_EPP
            Patriot_cp = vehicles.AirDefence.Patriot_cp
            Patriot_str = vehicles.AirDefence.Patriot_str
            NASAMS_Command_Post = vehicles.AirDefence.NASAMS_Command_Post
            NASAMS_Radar_MPQ64F1 = vehicles.AirDefence.NASAMS_Radar_MPQ64F1
            NASAMS_LN_B = vehicles.AirDefence.NASAMS_LN_B
            NASAMS_LN_C = vehicles.AirDefence.NASAMS_LN_C
            Gepard = vehicles.AirDefence.Gepard
            HQ_7_STR_SP = vehicles.AirDefence.HQ_7_STR_SP
            HQ_7_LN_SP = vehicles.AirDefence.HQ_7_LN_SP
            Igla_manpad_INS = vehicles.AirDefence.Igla_manpad_INS
            M6_Linebacker = vehicles.AirDefence.M6_Linebacker

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            SK_C_28_naval_gun = vehicles.Fortification.SK_C_28_naval_gun
            Fire_control = vehicles.Fortification.Fire_control

        class Unarmed:
            Blitz_36_6700A = vehicles.Unarmed.Blitz_36_6700A
            Kubelwagen_82 = vehicles.Unarmed.Kubelwagen_82
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40_kfz_21 = vehicles.Unarmed.Horch_901_typ_40_kfz_21
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            ATZ_10 = vehicles.Unarmed.ATZ_10
            GAZ_3307 = vehicles.Unarmed.GAZ_3307
            GAZ_66 = vehicles.Unarmed.GAZ_66
            IKARUS_Bus = vehicles.Unarmed.IKARUS_Bus
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            LAZ_Bus = vehicles.Unarmed.LAZ_Bus
            LiAZ_Bus = vehicles.Unarmed.LiAZ_Bus
            SKP_11 = vehicles.Unarmed.SKP_11
            Trolley_bus = vehicles.Unarmed.Trolley_bus
            UAZ_469 = vehicles.Unarmed.UAZ_469
            Ural_ATsP_6 = vehicles.Unarmed.Ural_ATsP_6
            Ural_375_PBU = vehicles.Unarmed.Ural_375_PBU
            Ural_375 = vehicles.Unarmed.Ural_375
            Ural_4320_APA_5D = vehicles.Unarmed.Ural_4320_APA_5D
            Ural_4320_31 = vehicles.Unarmed.Ural_4320_31
            Ural_4320T = vehicles.Unarmed.Ural_4320T
            VAZ_Car = vehicles.Unarmed.VAZ_Car
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG
            ZIL_4331 = vehicles.Unarmed.ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            ATZ_5 = vehicles.Unarmed.ATZ_5
            ZIL_135 = vehicles.Unarmed.ZIL_135
            ATZ_60_Maz = vehicles.Unarmed.ATZ_60_Maz
            TZ_22_KrAZ = vehicles.Unarmed.TZ_22_KrAZ
            AA8 = vehicles.Unarmed.AA8
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            M30_CC = vehicles.Unarmed.M30_CC
            Hummer = vehicles.Unarmed.Hummer
            KrAZ6322 = vehicles.Unarmed.KrAZ6322
            GAZ_3308 = vehicles.Unarmed.GAZ_3308
            MAZ_6303 = vehicles.Unarmed.MAZ_6303
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Predator_GCS = vehicles.Unarmed.Predator_GCS
            Predator_TrojanSpirit = vehicles.Unarmed.Predator_TrojanSpirit
            Tigr_233036 = vehicles.Unarmed.Tigr_233036

        class Armor:
            Pz_IV_H = vehicles.Armor.Pz_IV_H
            Sd_Kfz_251 = vehicles.Armor.Sd_Kfz_251
            Tiger_I = vehicles.Armor.Tiger_I
            Tiger_II_H = vehicles.Armor.Tiger_II_H
            Pz_V_Panther_G = vehicles.Armor.Pz_V_Panther_G
            Jagdpanther_G1 = vehicles.Armor.Jagdpanther_G1
            JagdPz_IV = vehicles.Armor.JagdPz_IV
            Stug_IV = vehicles.Armor.Stug_IV
            SturmPzIV = vehicles.Armor.SturmPzIV
            Sd_Kfz_234_2_Puma = vehicles.Armor.Sd_Kfz_234_2_Puma
            Stug_III = vehicles.Armor.Stug_III
            Elefant_SdKfz_184 = vehicles.Armor.Elefant_SdKfz_184
            BMD_1 = vehicles.Armor.BMD_1
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            BMP_3 = vehicles.Armor.BMP_3
            BRDM_2 = vehicles.Armor.BRDM_2
            BTR_D = vehicles.Armor.BTR_D
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            T_80UD = vehicles.Armor.T_80UD
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack
            Cromwell_IV = vehicles.Armor.Cromwell_IV
            Centaur_IV = vehicles.Armor.Centaur_IV
            M10_GMC = vehicles.Armor.M10_GMC
            Tetrarch = vehicles.Armor.Tetrarch
            PT_76 = vehicles.Armor.PT_76
            M4_Sherman = vehicles.Armor.M4_Sherman
            M4A4_Sherman_FF = vehicles.Armor.M4A4_Sherman_FF
            Churchill_VII = vehicles.Armor.Churchill_VII
            Daimler_AC = vehicles.Armor.Daimler_AC
            M8_Greyhound = vehicles.Armor.M8_Greyhound
            M4_Tractor = vehicles.Armor.M4_Tractor
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M_113 = vehicles.Armor.M_113
            TPZ = vehicles.Armor.TPZ
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_60 = vehicles.Armor.M_60
            M_1_Abrams = vehicles.Armor.M_1_Abrams
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto
            T_90 = vehicles.Armor.T_90
            Chieftain_mk3 = vehicles.Armor.Chieftain_mk3
            AAV7 = vehicles.Armor.AAV7
            Leopard1A3 = vehicles.Armor.Leopard1A3
            Leopard_2 = vehicles.Armor.Leopard_2
            Leopard_2A4 = vehicles.Armor.Leopard_2A4
            T_72B3 = vehicles.Armor.T_72B3
            BTR_82A = vehicles.Armor.BTR_82A
            M_2_Bradley = vehicles.Armor.M_2_Bradley
            Cobra = vehicles.Armor.Cobra
            LAV_25 = vehicles.Armor.LAV_25
            Merkava_Mk4 = vehicles.Armor.Merkava_Mk4
            Leopard_2A5 = vehicles.Armor.Leopard_2A5
            Marder = vehicles.Armor.Marder
            Leclerc = vehicles.Armor.Leclerc
            ZBD04A = vehicles.Armor.ZBD04A
            ZTZ96B = vehicles.Armor.ZTZ96B
            Leopard_2A4_trs = vehicles.Armor.Leopard_2A4_trs
            Challenger2 = vehicles.Armor.Challenger2
            M1126_Stryker_ICV = vehicles.Armor.M1126_Stryker_ICV
            M1128_Stryker_MGS = vehicles.Armor.M1128_Stryker_MGS
            M1134_Stryker_ATGM = vehicles.Armor.M1134_Stryker_ATGM
            MCV_80 = vehicles.Armor.MCV_80

        class MissilesSS:
            V1_launcher = vehicles.MissilesSS.V1_launcher
            Scud_B = vehicles.MissilesSS.Scud_B
            Hy_launcher = vehicles.MissilesSS.Hy_launcher
            Silkworm_SR = vehicles.MissilesSS.Silkworm_SR

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        Mirage_2000_5 = planes.Mirage_2000_5
        P_51D_30_NA = planes.P_51D_30_NA
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        H_6J = planes.H_6J
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.Mirage_2000_5,
        Plane.P_51D_30_NA,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.H_6J,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        Uboat_VIIC = ships.Uboat_VIIC
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        ALBATROS = ships.ALBATROS
        KILO = ships.KILO
        IMPROVED_KILO = ships.IMPROVED_KILO
        Dry_cargo_ship_1 = ships.Dry_cargo_ship_1
        Dry_cargo_ship_2 = ships.Dry_cargo_ship_2
        ELNYA = ships.ELNYA
        KUZNECOW = ships.KUZNECOW
        MOLNIYA = ships.MOLNIYA
        MOSCOW = ships.MOSCOW
        NEUSTRASH = ships.NEUSTRASH
        REZKY = ships.REZKY
        ZWEZDNY = ships.ZWEZDNY
        LST_Mk2 = ships.LST_Mk2
        USS_Samuel_Chase = ships.USS_Samuel_Chase
        Higgins_boat = ships.Higgins_boat
        HandyWind = ships.HandyWind
        Seawise_Giant = ships.Seawise_Giant
        PERRY = ships.PERRY
        PIOTR = ships.PIOTR
        CV_1143_5 = ships.CV_1143_5
        La_Combattante_II = ships.La_Combattante_II
        Type_052B = ships.Type_052B
        Type_052C = ships.Type_052C
        Type_054A = ships.Type_054A
        Type_071 = ships.Type_071
        Type_093 = ships.Type_093
        VINSON = ships.VINSON
        TICONDEROG = ships.TICONDEROG
        Stennis = ships.Stennis
        LHA_Tarawa = ships.LHA_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
        CVN_71 = ships.CVN_71
        CVN_72 = ships.CVN_72
        CVN_73 = ships.CVN_73
        CVN_75 = ships.CVN_75
        Forrestal = ships.Forrestal

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UnitedNationsPeacekeepers, self).__init__(UnitedNationsPeacekeepers.id, UnitedNationsPeacekeepers.name)


class Argentina(Country):
    id = 83
    name = "Argentina"

    class Vehicle:

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            Hummer = vehicles.Unarmed.Hummer
            M_818 = vehicles.Unarmed.M_818
            Trolley_bus = vehicles.Unarmed.Trolley_bus

        class Armor:
            AAV7 = vehicles.Armor.AAV7
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M_113 = vehicles.Armor.M_113
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        KC130 = planes.KC130
        B_17G = planes.B_17G
        F_86F_Sabre = planes.F_86F_Sabre
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.KC130,
        Plane.B_17G,
        Plane.F_86F_Sabre,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Argentina, self).__init__(Argentina.id, Argentina.name)


class Cyprus(Country):
    id = 84
    name = "Cyprus"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            SpGH_Dana = vehicles.Artillery.SpGH_Dana

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            S_300PS_40B6M_tr = vehicles.AirDefence.S_300PS_40B6M_tr
            S_300PS_40B6MD_sr = vehicles.AirDefence.S_300PS_40B6MD_sr
            S_300PS_54K6_cp = vehicles.AirDefence.S_300PS_54K6_cp
            S_300PS_5P85C_ln = vehicles.AirDefence.S_300PS_5P85C_ln
            S_300PS_5P85D_ln = vehicles.AirDefence.S_300PS_5P85D_ln
            S_300PS_64H6E_sr = vehicles.AirDefence.S_300PS_64H6E_sr
            SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SA_11_Buk_CC_9S470M1
            SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SA_11_Buk_LN_9A310M1
            SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SA_11_Buk_SR_9S18M1
            Tor_9A331 = vehicles.AirDefence.Tor_9A331
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            Ural_375_ZU_23 = vehicles.AirDefence.Ural_375_ZU_23
            Soldier_stinger = vehicles.AirDefence.Soldier_stinger

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT

        class Armor:
            BMP_3 = vehicles.Armor.BMP_3
            T_80UD = vehicles.Armor.T_80UD
            VAB_Mephisto = vehicles.Armor.VAB_Mephisto

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Mi_8MT = helicopters.Mi_8MT
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Mi_8MT,
        Helicopter.AH_64D_BLK_II,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Cyprus, self).__init__(Cyprus.id, Cyprus.name)


class Slovenia(Country):
    id = 85
    name = "Slovenia"

    class Vehicle:

        class Artillery:
            SAU_Gvozdika = vehicles.Artillery.SAU_Gvozdika

        class Infantry:
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Soldier_M4 = vehicles.Infantry.Soldier_M4

        class AirDefence:
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            Roland_Radar = vehicles.AirDefence.Roland_Radar
            Strela_1_9P31 = vehicles.AirDefence.Strela_1_9P31
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            M_818 = vehicles.Unarmed.M_818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Hummer = vehicles.Unarmed.Hummer
            M978_HEMTT_Tanker = vehicles.Unarmed.M978_HEMTT_Tanker

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            Cobra = vehicles.Armor.Cobra
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            MTLB = vehicles.Armor.MTLB
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.C_17A,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat
        MOLNIYA = ships.MOLNIYA

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Slovenia, self).__init__(Slovenia.id, Slovenia.name)


class Bolivia(Country):
    id = 86
    name = "Bolivia"

    class Vehicle:

        class Infantry:
            Soldier_M4 = vehicles.Infantry.Soldier_M4

        class AirDefence:
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            ATMZ_5 = vehicles.Unarmed.ATMZ_5
            Hummer = vehicles.Unarmed.Hummer
            KAMAZ_Truck = vehicles.Unarmed.KAMAZ_Truck
            M_818 = vehicles.Unarmed.M_818
            ZiL_131_APA_80 = vehicles.Unarmed.ZiL_131_APA_80
            ZIL_131_KUNG = vehicles.Unarmed.ZIL_131_KUNG

        class Armor:
            TPZ = vehicles.Armor.TPZ
            M_113 = vehicles.Armor.M_113
            M1043_HMMWV_Armament = vehicles.Armor.M1043_HMMWV_Armament
            M1045_HMMWV_TOW = vehicles.Armor.M1045_HMMWV_TOW
            M2A1_halftrack = vehicles.Armor.M2A1_halftrack

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        C_130 = planes.C_130
        F_86F_Sabre = planes.F_86F_Sabre
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_47 = planes.C_47
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.C_130,
        Plane.F_86F_Sabre,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_47,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Bolivia, self).__init__(Bolivia.id, Bolivia.name)


class Ghana(Country):
    id = 87
    name = "Ghana"

    class Vehicle:

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Armor:
            Cobra = vehicles.Armor.Cobra

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Ghana, self).__init__(Ghana.id, Ghana.name)


class Nigeria(Country):
    id = 88
    name = "Nigeria"

    class Vehicle:

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            Roland_ADS = vehicles.AirDefence.Roland_ADS
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Unarmed:
            KrAZ6322 = vehicles.Unarmed.KrAZ6322

        class Armor:
            BMP_1 = vehicles.Armor.BMP_1
            BMP_2 = vehicles.Armor.BMP_2
            Cobra = vehicles.Armor.Cobra
            T_55 = vehicles.Armor.T_55
            T_72B = vehicles.Armor.T_72B
            BTR_80 = vehicles.Armor.BTR_80
            MTLB = vehicles.Armor.MTLB

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        JF_17 = planes.JF_17
        L_39ZA = planes.L_39ZA
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.JF_17,
        Plane.L_39ZA,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Nigeria, self).__init__(Nigeria.id, Nigeria.name)


class Peru(Country):
    id = 89
    name = "Peru"

    class Vehicle:

        class Artillery:
            Grad_URAL = vehicles.Artillery.Grad_URAL
            M_109 = vehicles.Artillery.M_109

        class Infantry:
            Infantry_AK = vehicles.Infantry.Infantry_AK
            Infantry_AK_ver2 = vehicles.Infantry.Infantry_AK_ver2
            Infantry_AK_ver3 = vehicles.Infantry.Infantry_AK_ver3

        class AirDefence:
            Bofors40 = vehicles.AirDefence.Bofors40
            ZSU_23_4_Shilka = vehicles.AirDefence.ZSU_23_4_Shilka
            SA_18_Igla_S_comm = vehicles.AirDefence.SA_18_Igla_S_comm
            SA_18_Igla_S_manpad = vehicles.AirDefence.SA_18_Igla_S_manpad
            _5p73_s_125_ln = vehicles.AirDefence._5p73_s_125_ln
            P_19_s_125_sr = vehicles.AirDefence.P_19_s_125_sr
            Snr_s_125_tr = vehicles.AirDefence.Snr_s_125_tr
            ZU_23_Emplacement_Closed = vehicles.AirDefence.ZU_23_Emplacement_Closed
            ZU_23_Emplacement = vehicles.AirDefence.ZU_23_Emplacement

        class Fortification:
            Bunker = vehicles.Fortification.Bunker
            Sandbox = vehicles.Fortification.Sandbox
            House1arm = vehicles.Fortification.House1arm
            House2arm = vehicles.Fortification.House2arm
            Outpost_road = vehicles.Fortification.Outpost_road
            Outpost = vehicles.Fortification.Outpost
            HouseA_arm = vehicles.Fortification.HouseA_arm
            TACAN_beacon = vehicles.Fortification.TACAN_beacon

        class Armor:
            BRDM_2 = vehicles.Armor.BRDM_2
            M_113 = vehicles.Armor.M_113
            T_55 = vehicles.Armor.T_55
            M8_Greyhound = vehicles.Armor.M8_Greyhound

        class Locomotive:
            Electric_locomotive = vehicles.Locomotive.Electric_locomotive
            Locomotive = vehicles.Locomotive.Locomotive
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_cargo = vehicles.Carriage.Coach_cargo
            Coach_cargo_open = vehicles.Carriage.Coach_cargo_open
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_passenger = vehicles.Carriage.Coach_a_passenger
            Coach_a_platform = vehicles.Carriage.Coach_a_platform
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50Ton_Flat_Wagon = vehicles.Carriage.DR_50Ton_Flat_Wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        M_2000C = planes.M_2000C
        MiG_29S = planes.MiG_29S
        C_130 = planes.C_130
        KC130 = planes.KC130
        Su_17M4 = planes.Su_17M4
        Su_25 = planes.Su_25
        An_26B = planes.An_26B
        B_17G = planes.B_17G
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        MosquitoFBMkVI = planes.MosquitoFBMkVI
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        C_47 = planes.C_47

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.M_2000C,
        Plane.MiG_29S,
        Plane.C_130,
        Plane.KC130,
        Plane.Su_17M4,
        Plane.Su_25,
        Plane.An_26B,
        Plane.B_17G,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.MosquitoFBMkVI,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.C_47,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        AH_64D_BLK_II = helicopters.AH_64D_BLK_II
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.AH_64D_BLK_II,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Speedboat = ships.Speedboat

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Peru, self).__init__(Peru.id, Peru.name)


country_dict = {
    Russia.id: Russia,
    Ukraine.id: Ukraine,
    USA.id: USA,
    Turkey.id: Turkey,
    UK.id: UK,
    France.id: France,
    Germany.id: Germany,
    USAFAggressors.id: USAFAggressors,
    Canada.id: Canada,
    Spain.id: Spain,
    TheNetherlands.id: TheNetherlands,
    Belgium.id: Belgium,
    Norway.id: Norway,
    Denmark.id: Denmark,
    Israel.id: Israel,
    Georgia.id: Georgia,
    Insurgents.id: Insurgents,
    Abkhazia.id: Abkhazia,
    SouthOssetia.id: SouthOssetia,
    Italy.id: Italy,
    Australia.id: Australia,
    Switzerland.id: Switzerland,
    Austria.id: Austria,
    Belarus.id: Belarus,
    Bulgaria.id: Bulgaria,
    CzechRepublic.id: CzechRepublic,
    China.id: China,
    Croatia.id: Croatia,
    Egypt.id: Egypt,
    Finland.id: Finland,
    Greece.id: Greece,
    Hungary.id: Hungary,
    India.id: India,
    Iran.id: Iran,
    Iraq.id: Iraq,
    Japan.id: Japan,
    Kazakhstan.id: Kazakhstan,
    NorthKorea.id: NorthKorea,
    Pakistan.id: Pakistan,
    Poland.id: Poland,
    Romania.id: Romania,
    SaudiArabia.id: SaudiArabia,
    Serbia.id: Serbia,
    Slovakia.id: Slovakia,
    SouthKorea.id: SouthKorea,
    Sweden.id: Sweden,
    Syria.id: Syria,
    Yemen.id: Yemen,
    Vietnam.id: Vietnam,
    Venezuela.id: Venezuela,
    Tunisia.id: Tunisia,
    Thailand.id: Thailand,
    Sudan.id: Sudan,
    Philippines.id: Philippines,
    Morocco.id: Morocco,
    Mexico.id: Mexico,
    Malaysia.id: Malaysia,
    Libya.id: Libya,
    Jordan.id: Jordan,
    Indonesia.id: Indonesia,
    Honduras.id: Honduras,
    Ethiopia.id: Ethiopia,
    Chile.id: Chile,
    Brazil.id: Brazil,
    Bahrain.id: Bahrain,
    ThirdReich.id: ThirdReich,
    Yugoslavia.id: Yugoslavia,
    USSR.id: USSR,
    ItalianSocialRepublic.id: ItalianSocialRepublic,
    Algeria.id: Algeria,
    Kuwait.id: Kuwait,
    Qatar.id: Qatar,
    Oman.id: Oman,
    UnitedArabEmirates.id: UnitedArabEmirates,
    SouthAfrica.id: SouthAfrica,
    Cuba.id: Cuba,
    Portugal.id: Portugal,
    GDR.id: GDR,
    Lebanon.id: Lebanon,
    CombinedJointTaskForcesBlue.id: CombinedJointTaskForcesBlue,
    CombinedJointTaskForcesRed.id: CombinedJointTaskForcesRed,
    UnitedNationsPeacekeepers.id: UnitedNationsPeacekeepers,
    Argentina.id: Argentina,
    Cyprus.id: Cyprus,
    Slovenia.id: Slovenia,
    Bolivia.id: Bolivia,
    Ghana.id: Ghana,
    Nigeria.id: Nigeria,
    Peru.id: Peru,
}


def get_by_id(_id: int):
    """Returns a new country object for the given country id

    Args:
        _id: id for the country

    Returns:
        Country: a new country object
    """
    return country_dict[_id]()
