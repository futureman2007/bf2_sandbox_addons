NAME 	= "Projectiles"
VERSION = "2.0"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
DESCRIPTION = "Manages weapon modifying for projectiles."
COMMANDS = {
	"p": ["weapon","projectile","speed","rounds per minute","delay","Modifies a weapon's projectile settings."],
	"pthis": ["projectile","speed","rounds per minute","delay","Modifies your weapon's projectile settings."],
	"pall": ["projectile","speed","rounds per minute","delay","Modifies every weapon's projectile settings."],
	"preset": ["weapon","Restores default settings for the weapon you're using or one you request."],
	"presetall": ["Restores default settings for all modified weapons."],
	"prandomize": ["Gives each weapon a random projectile setting."],
	"pinfo": ["weapon","Gets information about a weapon's current state."],
	"pactive": ["weapon","Prepares a weapon for modifications."],
	"pproj": ["projectile","Sets a projectile for the active weapon."],
	"pspeed": ["speed","Modifies the projectile's speed."],
	"prpm": ["rounds per minute","Modifies the projectile's rounds per minute."],
	"pdelay": ["delay","Modifies the projectile's delay."]
}
 
DEFAULT_DATA = {
"aas_phalanx":					["Phalanx_Projectile",				"500",		"900",		None],
"aas_seasparrow":				["aim9m_sidewinder",				"20",		"120",		None],
"AAV_TUNGUSKA_Gun":				["AAV_TUNGUSKA_Gun_Projectile",			"500",		None,		None],
"aav_tunguska_SA19Launcher":			["sa19_grison",					"20",		"120",		None],
"AAV_TYPE95guns":				["AAV_TYPE95guns_Projectile",			"500",		None,		None],
"AAV_Type95_QW2Launcher":			["igla_9k38",					"20",		"120",		None],
"AHE_AH1Z_CoGunner_HellFireLauncherTV":		["agm114_hellfire_tv",				"75",		"60",		None],
"AHE_AH1Z_FlareLauncher":			["ahe_ah1z_flareLauncher_Projectile",		"10",		"1800",		None],
"AHE_AH1Z_Gun":					["AHE_AH1Z_Gun_Projectile",			"400",		None,		None],
"AHE_AH1Z_HydraLauncher":			["ahe_ah1z_HydraLauncher_Projectile",		"100",		None,		None],
"AHE_HAVOC_AtakaLauncher_TV":			["agm114_hellfire_tv",				"45",		"60",		None],
"ahe_havoc_FlareLauncher":			["ahe_havoc_FlareLauncher_Projectile",		"10",		"1800",		None],
"AHE_HAVOC_Gun":				["AHE_HAVOC_Gun_Projectile",			"400",		"300",		None],
"AHE_HAVOC_S8Launcher":				["ahe_havoc_S8Launcher_Projectile",		"100",		None,		None],
"ahe_z10_FlareLauncher":			["ahe_z10_flareLauncher_Projectile",		"10",		"1800",		None],
"AHE_Z10_Gun":					["AHE_Z10_Gun_Projectile",			"400",		None,		None],
"ahe_z10_HJ8Launcher_TV":			["agm114_hellfire_tv",				"45",		"60",		None],
"ahe_z10_S8Launcher":				["ahe_z10_S8Launcher_Projectile",		"100",		None,		None],
"air_a10_avenger_firearm":			["air_a10_Gun_Projectile",			"500",		"900",		None],
"air_a10_us_Bomblauncher":			["mk82_dumbbomb",				"0",		"300",		None],
"Air_F35b_AutoCannon":				["Air_F35b_AutoCannon_Projectile",		"500",		None,		None],
"air_f35b_bomblauncher":			["mk82_dumbbomb",				"0",		"150",		None],
"AIR_F35b_SidewinderLauncher":			["aim9m_sidewinder",				"75",		"120",		None],
"AIR_J10_ArcherLauncher":			["aa11_archer",					"75",		"120",		None],
"air_j10_bomblauncher":				["mec_250_bomb",				"0",		"150",		None],
"AIR_J10_Cannon":				["AIR_J10_Cannon_Projectile",			"500",		None,		None],
"AIR_SU30MKK_30mmCannon":			["AIR_SU30MKK_30mmCannon_Projectile",		"500",		None,		None],
"AIR_SU30MKK_ArcherLauncher":			["aa11_archer",					"75",		"120",		None],
"AIR_SU30MKK_KedgeLauncher_Laser":		["kh29_kedge",					"75",		"60",		None],
"AIR_SU30MKK_KedgeLauncher_Wire":		["kh29_kedge_tv",				"75",		"30",		None],
"AIR_SU34MKK_BombLauncher":			["mec_500_ret_bomb",				"0",		"300",		None],
"air_su39_Bomblauncher":			["mec_250_bomb",				"0",		"300",		None],
"air_su39_Canon":				["air_su39_Canon_Projectile",			"500",		"450",		None],
"ammokit":					["ammokit_Projectile",				"10",		None,		"0.7"],
"APC_BTR90_HJ8Launcher":			["tow_missile",					"40",		None,		None],
"APC_BTR90_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"APC_BTR90__Barrel":				["APC_BTR90__Barrel_Projectile",		"375",		"300",		None],
"APC_WZ551_Barrel":				["APC_WZ551_Barrel_Projectile",			"400",		"180",		None],
"APC_WZ551_HJ8Launcher":			["tow_missile",					"40",		None,		None],
"apc_wz551_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"ARS_D30_Barrel":				["ARS_D30_Barrel_Projectile",			"450",		"30",		None],
"ats_hj8_Launcher":				["tow_missile_stationary",			"20",		None,		None],
"ats_tow_Launcher":				["tow_missile_stationary",			"20",		None,		None],
"at_mine":					["at_mine_Projectile",				"5",		None,		"1.1"],
#"c4_detonator":				[None,						None,		"60",		None],
"c4_explosives":				["c4_explosives_Projectile",			"5",		None,		None],
"car_horn2":					["car_horn2_Projectile",			None,		None,		None],
"Car_horn":					["Car_horn_Projectile",				None,		None,		None],
"chat_eryx":					["eryx",					"30",		None,		"1.0"],
"che_wz11_Canons":				["che_wz11_Cannons_Projectile",			"500",		None,		None],
"che_wz11_FlareLauncher":			["che_wz11_flareLauncher_Projectile",		"10",		"1800",		None],
"chhmg_kord":					["CHHMG_KORD_Projectile",			"500",		"450",		None],
"chhmg_type85":					["chhmg_type85_Projectile",			"500",		"450",		None],
"chlmg_type95":					["chlmg_type95_Projectile",			"500",		"900",		"1.5"],
"chlmg_type95_stationary":			["chlmg_type95_stationary_Projectile",		"500",		"900",		None],
"chpis_qsz92":					["chpis_qsz92_Projectile",			"1000",		None,		"0.75"],
"chpis_qsz92_silencer":				["chpis_qsz92_silencer_Projectile",		"1000",		None,		"0.75"],
"chrif_type85":					["chrif_Type85_Projectile",			"1000",		"900",		"1.1"],
"chrif_type95":					["chrif_type95Projectile",			"1000",		None,		"0.916"],
"chsht_norinco982":				["chsht_norinco982_Projectile",			"1000",		"60",		"0.7"],
"chsht_protecta":				["chsht_protecta_Projectile",			"1000",		None,		"0.8"],
"chsni_type88":					["chsni_type88_Projectile",			"1000",		None,		"1"],
"chthe_z8_flarelauncher":			["chthe_z8_flarelauncher_Projectile",		"10",		"1800",		None],
"Coaxial_browning":				["Coax_Projectile",				"500",		None,		None],
"Coaxial_mg_china":				["Coaxial_mg_china_Projectile",			"500",		None,		None],
"Coaxial_mg_mec":				["Coaxial_mg_mec_Projectile",			"500",		None,		None],
"decoy_Flare_Launcher":				["decoy_flare_Launcher_Projectile",		"10",		"300",		None],
"defibrillator":				["defibrillator_Projectile",			"80",		None,		"0.4"],
"eurif_famas":					["eurif_famas_Projectile",			"1000",		"900",		"1.166"],
"eurif_fnp90":					["eurif_fnp90_Projectile",			"1000",		"900",		"1.2"],
"eurif_hk21":					["hk21Projectile",				"500",		None,		"1.625"],
"eurif_hk53a3":					["usrif_mp5_a3_Projectile",			"1000",		None,		"0.6"],
"Eurofighter_Autocannon":			["Eurofighter_Autocannon_Projectile",		"500",		None,		None],
"eurofighter_bomb_launcher":			["mk82_dumbbomb",				"0",		"150",		None],
"Eurofighter_Missiles":				["aim9m_sidewinder",				"75",		"120",		None],
"F18_Autocannon":				["F18_Autocannon_Projectile",			"500",		None,		None],
"F18_SidewinderLauncher":			["aim9m_sidewinder",				"75",		"120",		None],
"fantan_Autocannon":				["fantan_Autocannon_Projectile",		"500",		"450",		None],
"Firingport_AK":				["Firingport_AK_Projectile",			"1000",		None,		None],
"Firingport_M16":				["Firingport_M16_Projectile",			"1000",		None,		None],
"gbgr_sa80a2_l85":				["gbgr_sa80a2_l85_Projectile",			"50",		None,		"1.1"],
"gbrif_benelli_m4":				["gbrif_benelli_m4_Projectile",			"1000",		"300",		"1"],
"gbrif_l96a1":					["gbrif_l96a1_Projectile",			"1000",		None,		"1.6"],
"gbrif_sa80a2_l85":				["gbrif_sa80a2_l85_Projectile",			"1000",		None,		"1"],
"hgr_smoke":					["hgr_smoke_Projectile",			"20",		None,		"0.6"],
"hmg_m2hb":					["HMG_M2HB50cal_Projectile",			"500",		"450",		None],
"hmg_m2hb_ammo":				["hmg_m2hb_ammo_Projectile",			"0",		"450",		None],
"hmg_m134_br_Gun":				["hmg_m134_br_Projectile",			"500",		"900",		None],
"HMG_M134_Gun":					["HMG_M134_Projectile",				"500",		"900",		None],
"igla_djigit_Launcher":				["igla_9k38",					"80",		"120",		None],
"kni_knife":					["kni_knife_Projectile",			"40",		"120",		"0.6"],
"m249saw_ammo":					["m249saw_ammo_Projectile",			"0",		"450",		None],
"medikit":					["medikit_Projectile",				"10",		None,		"0.5"],
"nshgr_flashbang":				["nshgr_flashbang_Projectile",			"20",		None,		"0.7"],
"nsrif_crossbow":				["ziplineshell",				"1000",		None,		"1"],
"nsrif_grapplinghook":				["GrapplingHookRope",				"900",		None,		"0.9"],
#"ParachuteLauncher":				["Parachute",					"0",		None,		None],
"PlaneMG":					["PlaneMG_Projectile",				"1000",		None,		None],
"ruair_archerlauncher":				["aa11_archer",					"75",		"120",		None],
"ruair_mig29_30mmCannon":			["ruair_mig29_30mmCannon_Projectile",		"500",		None,		None],
"ruair_mig29_bomblauncher_1":			["mec_250_bomb",				"0",		"150",		None],
"ruair_su34_30mmCannon":			["ruair_su34_30mmCannon_Projectile",		"500",		None,		None],
"ruair_su34_250kgBombLauncher":			["mec_500_ret_bomb",				"0",		"300",		None],
"ruair_su34_archerlauncher":			["aa11_archer",					"75",		"120",		None],
"ruair_su34_KedgeLauncherLaser":		["kh29_kedge",					"45",		"30",		None],
"ruair_su34_KedgeLauncherTV":			["kh29_kedge_tv",				"45",		"30",		None],
"rulmg_pkm":					["RULMG_PKM_Projectile",			"500",		"450",		"1.83"],
"rulmg_rpk74":					["rpk74Projectile",				"500",		None,		"1.625"],
"rulmg_rpk74_stationary":			["rulmg_rpk74_stationary_projectile",		"500",		None,		None],
"rupis_baghira":				["RUPIS_Baghira_Projectile",			"1000",		None,		"0.75"],
"rupis_baghira_silencer":			["RUPIS_Baghira_silencer_Projectile",		"1000",		None,		"0.75"],
"rurgl_gp25":					["rurgl_gp25_Projectile",			"50",		None,		"1.208"],
"rurgl_gp30":					["RURGL_GP30_Projectile",			"50",		None,		"1.208"],
"rurif_ak47":					["rurif_ak47_Projectile",			"1000",		None,		"1.2"],
"rurif_ak101":					["RURIF_AK101_Projectile",			"1000",		None,		"0.666"],
"rurif_bizon":					["rurif_bizon_Projectile",			"1000",		"900",		None],
"rurif_dragunov":				["rurif_dragunov_Projectile",			"1000",		None,		"1"],
"rurif_gp25":					["rurif_gp25_Projectile",			"1000",		None,		"0.9"],
"rurif_gp30":					["RURIF_GP30_Projectile",			"1000",		None,		"0.666"],
"rurrif_ak74u":					["rurrif_ak74u_Projectile",			"1000",		None,		"1.208"],
"rusht_saiga12":				["rusht_saiga12_Projectile",			"1000",		None,		"1.2"],
"RUTNK_T90_Barrel":				["T90GunProjectile",				"150",		"30",		None],
"RUTNK_T90_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"sasgr_fn2000":					["sasgr_fn2000_Projectile",			"50",		None,		"1.166"],
"sasrif_fn2000":				["sasrif_fn2000_Projectile",			"1000",		"600",		"1.166"],
"sasrif_g36e":					["sasrif_g36e_Projectile",			"1000",		"900",		"1.166"],
"sasrif_mg36":					["sasrif_mg36_Projectile",			"500",		None,		"1.5"],
"sasrif_mp7":					["sasrif_mp7_Projectile",			"1000",		"900",		"1.2"],
"she_ec635_Cannons":				["she_ec635_Cannons_Projectile",		"500",		None,		None],
"she_ec635_FlareLauncher":			["she_ec635_flareLauncher_Projectile",		"10",		"1800",		None],
"she_littlebird_FlareLauncher":			["she_littlebird_flareLauncher_Projectile",	"10",		"1800",		None],
"she_littlebird_miniguns":			["she_littlebird_miniguns_Projectile",		"500",		None,		None],
#"simrad":					[None,						"1000",		None,		"0.958"],
"the_mi17_flarelauncher":			["the_mi17_flarelauncher_Projectile",		"50",		"1800",		None],
"tnk_c2_barrel":				["xpak2_tnkc2_Barrel_Projectile",		"150",		"30",		None],
"tnk_l2a6_barrel":				["tnk_l2a6_barrel_Projectile",			"150",		"30",		None],
"tnk_l2a6_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"TNK_Type98_Barrel":				["Type98GunProjectile",				"150",		"30",		None],
"TNK_Type98_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"truck_horn":					["truck_horn_Projectile",			None,		None,		None],
"USAAS_Stinger_Launcher":			["igla_9k38",					"20",		"120",		None],
"USAAV_M6_Barrel":				["USAAV_M6_Barrel_Projectile",			"500",		"225",		None],
"USAAV_M6_Stinger_Launcher":			["igla_9k38",					"20",		"120",		None],
"usair_f15_250kgbomblauncher":			["mk82_500_ret_bomb",				"0",		"300",		None],
"USAIR_F15_AutoCannon":				["USAIR_F15_AutoCannon_Projectile",		"500",		None,		None],
"USAIR_F15_MaverickLauncherLaser":		["agm65_maverick",				"45",		"60",		None],
"USAIR_F15_MaverickLauncherTV":			["agm65_maverick_tv",				"45",		"30",		None],
"USAIR_F15_SidewinderLauncher":			["aim9m_sidewinder",				"75",		"120",		None],
"usair_f18_bomblauncher":			["mk82_dumbbomb",				"0",		"150",		None],
"USAPC_LAV25_Barrel":				["USAPC_LAV25_Barrel_Projectile",		"375",		"225",		None],
"USAPC_LAV25_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"USAPC_LAV25_TowLauncher":			["tow_missile",					"40",		None,		None],
"USART_LW155_Barrel":				["USART_LW155_Barrel_Projectile",		"450",		"30",		None],
"usatp_predator":				["at_predator",					"30",		None,		"1"],
"ushgr_m67":					["ushgr_m67_Projectile",			"25",		None,		"0.6"],
"uslmg_m249saw":				["m249Projectile",				"500",		"900",		"1.625"],
"uslmg_m249saw_stationary":			["uslmg_m249saw_stationary_Projectile",		"500",		"900",		None],
"usmin_claymore":				["usmin_claymore_Projectile",			"5",		None,		"1"],
"uspis_92fs":					["USPIS_92FS_Projectile",			"1000",		None,		"0.75"],
"uspis_92fs_tracer":				["USPIS_92FS_Projectile",			"1000",		None,		"0.75"],
"uspis_92fs_silencer":				["USPIS_92FS_silencer_Projectile",		"1000",		None,		"0.75"],
"usrgl_m203":					["USRGL_M203_Projectile",			"50",		None,		"1.583"],
"usrif_fnscarl":				["usrif_fnscarl_Projectile",			"1000",		None,		"1.166"],
"usrif_g3a3":					["g3a3_Projectile",				"1000",		None,		"1.166"],
"usrif_g36c":					["G36C_Projectile",				"1000",		"600",		"1.166"],
"usrif_m4":					["M4Projectile",				"1000",		None,		"1.166"],
"usrif_m16a2":					["M16a2Projectile",				"1000",		"900",		"1.166"],
"usrif_m24":					["usrif_m24_Projectile",			"1000",		None,		"1.6"],
"usrif_m203":					["USRIF_M203_Projectile",			"1000",		"900",		"0.7"],
"usrif_mp5_a3":					["usrif_mp5_a3_Projectile",			"1000",		"900",		"0.6"],
"usrif_remington11-87":				["usrif_remington11-87_Projectile",		"1000",		"60",		"1"],
"usrif_sa80":					["usrif_sa80_Projectile",			"1000",		None,		"1"],
"ussht_jackhammer":				["JackhammerProjectile",			"1000",		"300",		"1.33"],
"ussni_m82a1":					["M82a1Projectile",				"1000",		"450",		None],
"ussni_m95_barret":				["USSNI_M95_Barret_Projectile",			"1000",		None,		"1"],
"usthe_uh60_flarelauncher":			["usthe_uh60_flarelauncher_Projectile",		"10",		"1800",		None],
"USTNK_M1A2_Barrel":				["USTNK_M1A2_Barrel_Projectile",		"150",		"30",		None],
"USTNK_M1A2_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"veh_tow_Launcher":				["tow_missile",					"20",		None,		None],
"wrench2":					["BlankProjectile",				"1000",		"60",		"0.958"],
"wrench":					["BlankProjectile",				"1000",		"60",		"0.958"],
"xpak2_fantan_bomblauncher":			["mec_250_bomb",				"0",		"150",		None],
"xpak2_tiger_FlareLauncher":			["xpak2_tiger_flareLauncher_Projectile",	"10",		"1800",		None],
"xpak2_tiger_Gun":				["xpak2_tiger_Gun_Projectile",			"400",		"300",		None],
"xpak2_Tiger_Hellfire_TV":			["agm114_hellfire_tv",				"45",		"60",		None],
"xpak2_tiger_Missiles":				["xpak2_tiger_Missiles_Projectile",		"100",		None,		None],
"xpak2_tnkc2_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"xpak_apache_FlareLauncher":			["xpak_apache_flareLauncher_Projectile",	"10",		"1800",		None],
"xpak_Apache_GunShot":				["xpak_Apache_GunShot_Projectile",		"400",		None,		None],
"xpak_apache_Hellfire_TV":			["agm114_hellfire_tv",				"45",		"60",		None],
"xpak_apache_S8Launcher_GenericFireArm":	["hydra_70",					"100",		None,		None],
"xpak_hind_GenericFireArm_Hydra":		["hydra_70",					"100",		"300",		None],
"xpak_bmp3_Maingun":				["xpak_bmp3_Maingun_Projectile",		"150",		"30",		None],
"xpak_bmp3_SmokeLauncher":			["Smokeflare",					"12",		"1800",		None],
"xpak_hind_FlareLauncher":			["xpak_hind_flareLauncher_Projectile",		"10",		"1800",		None],
"xpak_hind_GenericFireArm_Hydra":		["hydra_70",					"100",		"300",		None],
"xpak_hind_GenericFireArm_MG":			["xpak_hind_GenericFireArm_MG_Projectile",	"400",		None,		None],
"xpak_hind_missiles_tv":			["agm114_hellfire_tv",				"45",		"60",		None]}
 
PROJECTILE_DATA = {
"aa11_archer":					["archer"],
#"aa11_archerdummy":				["archerdummy"],
"AAV_TUNGUSKA_Gun_Projectile":			["tunguska"],
"AAV_TYPE95guns_Projectile":			["type95"],
"agm65_maverick":				["maverick"],
#"agm65_maverickdummy":				["maverickdummy"],
"agm65_maverick_dumb":				["maverickdumb"],
"agm65_maverick_tv":				["tv"],
"agm114_hellfire":				["hellfire"],
#"agm114_hellfiredummy":			["hellfiredummy"],
#"agm114_hellfire_tv":				["tv3"],
"ahe_ah1z_flareLauncher_Projectile":		["flare"],
"AHE_AH1Z_Gun_Projectile":			["cobra"],
"ahe_ah1z_HydraLauncher_Projectile":		["missile"],
"ahe_havoc_FlareLauncher_Projectile":		["flare2"],
"AHE_HAVOC_Gun_Projectile":			["havoc"],
"ahe_havoc_S8Launcher_Projectile":		["havocs8"],
"ahe_z10_flareLauncher_Projectile":		["flare3"],
"AHE_Z10_Gun_Projectile":			["z10"],
"ahe_z10_S8Launcher_Projectile":		["z10s8"],
"aim9m_sidewinder":				["sidewinder","aa"],
#"aim9m_sidewinderdummy":			["sidewinderdummy"],
"air_a10_Gun_Projectile":			["a10"],
"Air_F35b_AutoCannon_Projectile":		["f35b"],
"AIR_J10_Cannon_Projectile":			["j10"],
"AIR_SU30MKK_30mmCannon_Projectile":		["su30"],
"air_su39_Canon_Projectile":			["su39"],
"ammokit_Projectile":				["ammo"],
"APC_BTR90__Barrel_Projectile":			["btr90"],
"APC_WZ551_Barrel_Projectile":			["wz551"],
"ARS_D30_Barrel_Projectile":			["artillery2"],
"at_mine_Projectile":				["mine"],
"at_predator":					["predator"],
"BlankProjectile":				["Blank"],
"c4_explosives_Projectile":			["c4"],
"car_horn2_Projectile":				["horn2"],
"Car_horn_Projectile":				["horn"],
"che_wz11_Cannons_Projectile":			["wz11"],
"che_wz11_flareLauncher_Projectile":		["flare4"],
"CHHMG_KORD_Projectile":			["kord"],
"chhmg_type85_Projectile":			["type85mg"],
"chlmg_type95_Projectile":			["type95mg"],
"chlmg_type95_stationary_Projectile":		["type95mgwall"],
"chpis_qsz92_Projectile":			["qsz92"],
"chpis_qsz92_silencer_Projectile":		["qsz92silencer"],
"chrif_Type85_Projectile":			["type85rifle"],
"chrif_type95Projectile":			["type95rifle"],
"chsht_norinco982_Projectile":			["norinco982"],
"chsht_protecta_Projectile":			["protecta"],
"chsni_type88_Projectile":			["type88sniper"],
"chthe_z8_flarelauncher_Projectile":		["flare5"],
"Coaxial_mg_china_Projectile":			["chinacoaxialmg"],
"Coaxial_mg_mec_Projectile":			["meccoaxialmg"],
"Coax_Projectile":				["coax"],
"crossbow_bolt":				["crossbow"],
"decoy_flare_Launcher_Projectile":		["flare6"],
"defibrillator_Projectile":			["defibrillator"],
"eryx":						["eryx"],
#"eryxdummy":					["eryxdummy"],
"eurif_famas_Projectile":			["famasrifle"],
"eurif_fnp90_Projectile":			["fnp90rifle"],
"Eurofighter_Autocannon_Projectile":		["eurofighter"],
"F18_Autocannon_Projectile":			["f18"],
"fantan_Autocannon_Projectile":			["fantan"],
"Firingport_AK_Projectile":			["ak"],
"Firingport_M16_Projectile":			["m16"],
"g3a3_Projectile":				["g3a3"],
"G36C_Projectile":				["g36c"],
"gbgr_sa80a2_l85_Projectile":			["sa80a2gr","miniartillery","miniarty"],
"gbrif_benelli_m4_Projectile":			["benelli"],
"gbrif_l96a1_Projectile":			["l96a1"],
"gbrif_sa80a2_l85_Projectile":			["sa80a2rifle"],
"GrapplingHookRope":				["grapplinghook"],
"hgr_smoke_Projectile":				["smokegrenade"],
"hk21Projectile":				["hk21"],
"HMG_M2HB50cal_Projectile":			["m2hb50cal"],
"hmg_m2hb_ammo_Projectile":			["m2hbammo"],
"hmg_m134_br_Projectile":			["m134br"],
"HMG_M134_Projectile":				["m134"],
"hydra_70":					["hydra"],
#"hydra_70dummy":				["hydradummy"],
"igla_9k38":					["igla","aa2"],
"JackhammerProjectile":				["jackhammer"],
"kh29_kedge":					["kedge"],
#"kh29_kedgedummy":				["kedgedummy"],
"kh29_kedge_dumb":				["kedgedumb"],
"kh29_kedge_tv":				["tv2"],
"kni_knife_Projectile":				["knife"],
"M4Projectile":					["m4"],
"M16a2Projectile":				["m16a2"],
"M82a1Projectile":				["m82a1"],
"m249Projectile":				["m249"],
"m249saw_ammo_Projectile":			["m249ammo"],
"mec_250_bomb":					["bomb"],
#"mec_250_bombdummy":				["bombdummy"],
"mec_500_ret_bomb":				["bomb2"],
#"mec_500_ret_bomb_dummy":			["bomb2dummy"],
"medikit_Projectile":				["medicbox","medic"],
"mk82_500_ret_bomb":				["bomb3"],
"mk82_dumbbomb":				["bomb3dumb"],
#"mk82_dumbbombdummy":				["bomb3dummy"],
"nshgr_flashbang_Projectile":			["flash"],
#"Parachute":					["parachute"],
"Phalanx_Projectile":				["phalanx"],
"PlaneMG_Projectile":				["plane"],
"rpk74Projectile":				["rpk74"],
"ruair_mig29_30mmCannon_Projectile":		["mig29"],
"ruair_su34_30mmCannon_Projectile":		["su34"],
"RULMG_PKM_Projectile":				["pkm"],
"rulmg_rpk74_stationary_projectile":		["rpk74wall"],
"RUPIS_Baghira_Projectile":			["baghira"],
"RUPIS_Baghira_silencer_Projectile":		["baghirasilencer"],
"rurgl_gp25_Projectile":			["gp25","miniartillery2","miniarty2"],
"RURGL_GP30_Projectile":			["gp30"],
"rurif_ak47_Projectile":			["ak47"],
"RURIF_AK101_Projectile":			["ak101"],
"rurif_bizon_Projectile":			["bizon"],
"rurif_dragunov_Projectile":			["dragunov"],
"rurif_gp25_Projectile":			["gp25rifle"],
"RURIF_GP30_Projectile":			["gp30rifle"],
"rurrif_ak74u_Projectile":			["ak74u"],
"rusht_saiga12_Projectile":			["saiga12"],
"sa19_grison":					["grison","aa3"],
"sasgr_fn2000_Projectile":			["fn2000gr","miniartillery3","miniarty3"],
"sasrif_fn2000_Projectile":			["fn2000rifle"],
"sasrif_g36e_Projectile":			["g36e"],
"sasrif_mg36_Projectile":			["mg36"],
"sasrif_mp7_Projectile":			["mp7"],
"she_ec635_Cannons_Projectile":			["ec635"],
"she_ec635_flareLauncher_Projectile":		["flare7"],
"she_littlebird_flareLauncher_Projectile":	["flare8"],
"she_littlebird_miniguns_Projectile":		["littlebird"],
"Smokeflare":					["smoke"],
"T90GunProjectile":				["t90"],
"the_mi17_flarelauncher_Projectile":		["flare9"],
"tnk_l2a6_barrel_Projectile":			["tank"],
"tow_missile":					["tow"],
"tow_missile_stationary":			["towwall"],
"truck_horn_Projectile":			["horn3"],
"Type98GunProjectile":				["type98"],
"USAAV_M6_Barrel_Projectile":			["m6"],
"USAIR_F15_AutoCannon_Projectile":		["f15"],
"USAPC_LAV25_Barrel_Projectile":		["lav25"],
"USART_LW155_Barrel_Projectile":		["artillery"],
"ushgr_m67_Projectile":				["m67","grenade"],
"uslmg_m249saw_stationary_Projectile":		["m249saw"],
"usmin_claymore_Projectile":			["claymore"],
"USPIS_92FS_Projectile":			["pistol2"],
"uspis_92fs_tracer_Projectile":			["pistol"],
"USPIS_92FS_silencer_Projectile":		["92fssilencer"],
"USRGL_M203_Projectile":			["m203"],
"usrif_fnscarl_Projectile":			["fnscarl"],
"usrif_m24_Projectile":				["m24"],
"USRIF_M203_Projectile":			["m203rifle"],
"usrif_mp5_a3_Projectile":			["mp5"],
"usrif_remington11-87_Projectile":		["remington"],
"usrif_sa80_Projectile":			["sa80"],
"USSNI_M95_Barret_Projectile":			["m95"],
"usthe_uh60_flarelauncher_Projectile":		["flare10"],
"USTNK_M1A2_Barrel_Projectile":			["tank2"],
"xpak2_tiger_flareLauncher_Projectile":		["flare11"],
"xpak2_tiger_Gun_Projectile":			["tiger"],
"xpak2_tiger_Missiles_Projectile":		["missile2"],
"xpak2_tnkc2_Barrel_Projectile":		["tank3"],
"xpak_apache_flareLauncher_Projectile":		["flare12"],
"xpak_Apache_GunShot_Projectile":		["apache"],
"xpak_bmp3_Maingun_Projectile":			["bmp3"],
"xpak_hind_flareLauncher_Projectile":		["flare13"],
"xpak_hind_GenericFireArm_MG_Projectile":	["hind"],
"ziplineshell":					["zipline"]}
 
WEAPON_DATA = {
"aas_phalanx":					["phalanx"],
"aas_seasparrow":				["seasparrow"],
"AAV_TUNGUSKA_Gun":				["tunguska"],
"aav_tunguska_SA19Launcher":			["tunguskamissile"],
"AAV_TYPE95guns":				["aavtype95"],
"AAV_Type95_QW2Launcher":			["aavtype95missile"],
"AHE_AH1Z_CoGunner_HellFireLauncherTV":		["cobratv"],
"AHE_AH1Z_FlareLauncher":			["cobraflares"],
"AHE_AH1Z_Gun":					["cobra"],
"AHE_AH1Z_HydraLauncher":			["cobramissiles"],
"AHE_HAVOC_AtakaLauncher_TV":			["havoctv"],
"ahe_havoc_FlareLauncher":			["havocflares"],
"AHE_HAVOC_Gun":				["havoc"],
"AHE_HAVOC_S8Launcher":				["havocmissiles"],
"ahe_z10_FlareLauncher":			["z10flares"],
"AHE_Z10_Gun":					["z10"],
"ahe_z10_HJ8Launcher_TV":			["z10tv"],
"ahe_z10_S8Launcher":				["z10missiles"],
"air_a10_avenger_firearm":			["a10"],
"air_a10_us_Bomblauncher":			["a10bombs"],
"Air_F35b_AutoCannon":				["f35b"],
"air_f35b_bomblauncher":			["f35bbombs"],
"AIR_F35b_SidewinderLauncher":			["f35bmissiles"],
"AIR_J10_ArcherLauncher":			["j10missiles"],
"air_j10_bomblauncher":				["j10bombs"],
"AIR_J10_Cannon":				["j10"],
"AIR_SU30MKK_30mmCannon":			["su30"],
"AIR_SU30MKK_ArcherLauncher":			["su30missiles"],
"AIR_SU30MKK_KedgeLauncher_Laser":		["su30laser"],
"AIR_SU30MKK_KedgeLauncher_Wire":		["su30wire"],
"AIR_SU34MKK_BombLauncher":			["su30missiles"],
"air_su39_Bomblauncher":			["su39bombs"],
"air_su39_Canon":				["su39"],
"ammokit":					["ammo"],
"APC_BTR90_HJ8Launcher":			["btr90missile"],
"APC_BTR90_SmokeLauncher":			["btr90smoke"],
"APC_BTR90__Barrel":				["btr90"],
"APC_WZ551_Barrel":				["wz551"],
"APC_WZ551_HJ8Launcher":			["wz551missile"],
"apc_wz551_SmokeLauncher":			["wz551smoke"],
"ARS_D30_Barrel":				["artillery2"],
"ats_hj8_Launcher":				["tow2"],
"ats_tow_Launcher":				["tow"],
"at_mine":					["mine"],
#"c4_detonator":				["c4detonator"],
"c4_explosives":				["c4"],
"car_horn2":					["horn2"],
"Car_horn":					["horn"],
"chat_eryx":					["eryx"],
"che_wz11_Canons":				["wz11"],
"che_wz11_FlareLauncher":			["wz11flares"],
"chhmg_kord":					["kord"],
"chhmg_type85":					["type85mg"],
"chlmg_type95":					["type95mg"],
"chlmg_type95_stationary":			["type95mgwall"],
"chpis_qsz92":					["qsz92"],
"chpis_qsz92_silencer":				["qsz92silencer"],
"chrif_type85":					["type85rifle"],
"chrif_type95":					["type95rifle"],
"chsht_norinco982":				["norinco982"],
"chsht_protecta":				["protecta"],
"chsni_type88":					["type88"],
"chthe_z8_flarelauncher":			["z8flares"],
"Coaxial_browning":				["coaxial"],
"Coaxial_mg_china":				["chinacoaxial"],
"Coaxial_mg_mec":				["meccoaxial"],
"decoy_Flare_Launcher":				["flares"],
"defibrillator":				["defib"],
"eurif_famas":					["famasrifle"],
"eurif_fnp90":					["fnp90rifle"],
"eurif_hk21":					["hk21rifle"],
"eurif_hk53a3":					["hk53a3rifle"],
"Eurofighter_Autocannon":			["eurofighter"],
"eurofighter_bomb_launcher":			["eurofighterbombs"],
"Eurofighter_Missiles":				["eurofightermissiles"],
"F18_Autocannon":				["f18"],
"F18_SidewinderLauncher":			["f18missiles"],
"fantan_Autocannon":				["fantan"],
"Firingport_AK":				["ak"],
"Firingport_M16":				["m16"],
"gbgr_sa80a2_l85":				["sa80a2gr"],
"gbrif_benelli_m4":				["benellirifle"],
"gbrif_l96a1":					["l96a1rifle"],
"gbrif_sa80a2_l85":				["sa80a2rifle"],
"hgr_smoke":					["smokegrenade"],
"hmg_m2hb":					["m2hb"],
"hmg_m2hb_ammo":				["ammo"],
"hmg_m134_br_Gun":				["m134br"],
"HMG_M134_Gun":					["m134"],
"igla_djigit_Launcher":				["igla"],
"kni_knife":					["knife"],
"m249saw_ammo":					["m249saw"],
"medikit":					["medicbox","medic"],
"nshgr_flashbang":				["flashgrenade"],
"nsrif_crossbow":				["zipline"],
"nsrif_grapplinghook":				["grapplinghook"],
#"ParachuteLauncher":				["parachute"],
"PlaneMG":					["plane"],
"ruair_archerlauncher":				["archer"],
"ruair_mig29_30mmCannon":			["mig29"],
"ruair_mig29_bomblauncher_1":			["mig29bombs"],
"ruair_su34_30mmCannon":			["su34"],
"ruair_su34_250kgBombLauncher":			["su34bombs"],
"ruair_su34_archerlauncher":			["su34missiles"],
"ruair_su34_KedgeLauncherLaser":		["su34laser"],
"ruair_su34_KedgeLauncherTV":			["su34tv"],
"rulmg_pkm":					["pkm"],
"rulmg_rpk74":					["rpk74"],
"rulmg_rpk74_stationary":			["rpk74wall"],
"rupis_baghira":				["baghira"],
"rupis_baghira_silencer":			["baghirasilencer"],
"rurgl_gp25":					["gp25"],
"rurgl_gp30":					["gp30"],
"rurif_ak47":					["ak47"],
"rurif_ak101":					["ak101"],
"rurif_bizon":					["bizon"],
"rurif_dragunov":				["dragunov"],
"rurif_gp25":					["gp25rifle"],
"rurif_gp30":					["gp30rifle"],
"rurrif_ak74u":					["ak74urifle"],
"rusht_saiga12":				["saiga12"],
"RUTNK_T90_Barrel":				["t90"],
"RUTNK_T90_SmokeLauncher":			["t90smoke"],
"sasgr_fn2000":					["fn2000gr"],
"sasrif_fn2000":				["fn2000rifle"],
"sasrif_g36e":					["g36erifle"],
"sasrif_mg36":					["mg36rifle"],
"sasrif_mp7":					["mp7rifle"],
"she_ec635_Cannons":				["ec635"],
"she_ec635_FlareLauncher":			["ec635flares"],
"she_littlebird_FlareLauncher":			["littlebirdflares"],
"she_littlebird_miniguns":			["littlebird"],
#"simrad":					["simrad"],
"the_mi17_flarelauncher":			["mi17flares"],
"tnk_c2_barrel":				["c2"],
"tnk_l2a6_barrel":				["l2a6"],
"tnk_l2a6_SmokeLauncher":			["l2a6smoke"],
"TNK_Type98_Barrel":				["type98"],
"TNK_Type98_SmokeLauncher":			["type98smoke"],
"truck_horn":					["truckhorn"],
"USAAS_Stinger_Launcher":			["stinger"],
"USAAV_M6_Barrel":				["m6"],
"USAAV_M6_Stinger_Launcher":			["m6missiles"],
"usair_f15_250kgbomblauncher":			["f15bombs"],
"USAIR_F15_AutoCannon":				["f15"],
"USAIR_F15_MaverickLauncherLaser":		["f15laser"],
"USAIR_F15_MaverickLauncherTV":			["f15tv"],
"USAIR_F15_SidewinderLauncher":			["f15missiles"],
"usair_f18_bomblauncher":			["f18bombs"],
"USAPC_LAV25_Barrel":				["lav25"],
"USAPC_LAV25_SmokeLauncher":			["lav25smoke"],
"USAPC_LAV25_TowLauncher":			["lav25missile"],
"USART_LW155_Barrel":				["artillery"],
"usatp_predator":				["predator"],
"ushgr_m67":					["m67","grenade"],
"uslmg_m249saw":				["m249saw"],
"uslmg_m249saw_stationary":			["m249sawwall"],
"usmin_claymore":				["claymore"],
"uspis_92fs":					["pistol2"],
"uspis_92fs_tracer":				["pistol"],
"uspis_92fs_silencer":				["92fssilencer"],
"usrgl_m203":					["m203"],
"usrif_fnscarl":				["fnscarl"],
"usrif_g3a3":					["g3a3"],
"usrif_g36c":					["g36c"],
"usrif_m4":					["m4"],
"usrif_m16a2":					["m16a2"],
"usrif_m24":					["m24"],
"usrif_m203":					["m203rifle"],
"usrif_mp5_a3":					["mp5"],
"usrif_remington11-87":				["remington"],
"usrif_sa80":					["sa80"],
"ussht_jackhammer":				["jackhammer"],
"ussni_m82a1":					["m82a1"],
"ussni_m95_barret":				["m95"],
"usthe_uh60_flarelauncher":			["uh60flares"],
"USTNK_M1A2_Barrel":				["m1a2"],
"USTNK_M1A2_SmokeLauncher":			["m1a2smoke"],
"veh_tow_Launcher":				["tow"],
"wrench2":					["wrench"],
"wrench":					["wrench2"],
"xpak2_fantan_bomblauncher":			["fantanbombs"],
"xpak2_tiger_FlareLauncher":			["fantanflares"],
"xpak2_tiger_Gun":				["tiger"],
"xpak2_Tiger_Hellfire_TV":			["tigertv"],
"xpak2_tiger_Missiles":				["tivermissiles"],
"xpak2_tnkc2_SmokeLauncher":			["c2smoke"],
"xpak_apache_FlareLauncher":			["apacheflares"],
"xpak_Apache_GunShot":				["apache"],
"xpak_apache_Hellfire_TV":			["apachetv"],
"xpak_apache_S8Launcher_GenericFireArm":	["apachemissiles"],
"xpak_bmp3_Maingun":				["bmp3"],
"xpak_bmp3_SmokeLauncher":			["bmp3smoke"],
"xpak_hind_FlareLauncher":			["hindflares"],
"xpak_hind_GenericFireArm_Hydra":		["hindmissiles"],
"xpak_hind_GenericFireArm_MG":			["hind"],
"xpak_hind_missiles_tv":			["hindtv"]}
 
import random
import host
import copy
 
class Addon:
 
	def __init__(self, core):
		self.core = core
		self.silent = False
		self.modifiedWeapons = []
		self.CURRENT_DATA = copy.deepcopy(DEFAULT_DATA)
 
	def onPlayerConnect(self, playerObject):
		playerObject.activeWeapon = None
 
	def onGameStatusChanged(self, status):
		self.silent = False
		self.modifiedWeapons = []
		self.CURRENT_DATA = copy.deepcopy(DEFAULT_DATA)
 
	def chat_p(self, p, params):
		self.processData(params)
		p.activeWeapon = params[0]
 
	def chat_pthis(self, p, params):
		params.reverse()
		try:
			params.append(p.getPrimaryWeapon().templateName)
		except:
			self.sendMsg("ERROR - No weapon selected.")
			return
		params.reverse()
		self.processData(params)
		p.activeWeapon = params[0]
 
	def chat_pall(self, p, params):
		self.silent = True
		for i in WEAPON_DATA.keys():
			data = [i]
			for x in params:
				data.append(x)
			try:
				self.processData(data)
			except:
				p.sendMsg("ERROR - " + str(data))
		self.silent = False
		params[0] = self.getName(params[0], PROJECTILE_DATA)
		string = ["Projectile: ", "Velocity: ", "RPM: ", "Delay: "]
		gold = "低1001"
		finalString = "All weapons"
		for i in range(0, 4):
			value = True
			if i > 0:
				try: params[i] = str(float(params[i]))
				except: value = False
			if value:
				if len(params) >= i + 1:
					if params[i]:
						finalString += " - " + string[i] + gold + params[i] + gold
		self.sendMsg(finalString + ".")
 
	def chat_prandomize(self, p, params):
		self.silent = True
		for i in WEAPON_DATA.keys():
			data = [i, PROJECTILE_DATA.keys()[random.randint(0, len(PROJECTILE_DATA.keys()) - 1)], str(random.randint(0, 500)), str(random.randint(0, 1000)), "0"]
			try:
				self.processData(data)
			except:
				p.sendMsg("ERROR - " + str(data))
		self.silent = False
		self.sendMsg("Weapons randomized.")
 
	def chat_preset(self, p, params):
		weapon = None
		if len(params) > 0:
			weapon = self.getName(params[0], WEAPON_DATA)
			if not weapon:
				self.sendMsg("ERROR - Bad weapon name (低1001" + params[0] + "低1001).")
				return
		else:
			try: weapon = p.getPrimaryWeapon().templateName
			except:
				self.sendMsg("ERROR - No weapon selected.")
				return
		data = self.defaultValues(weapon)
		self.processData([weapon, data[0], data[1], data[2], data[3]])
		if weapon in self.modifiedWeapons: self.modifiedWeapons.remove(weapon)
 
	def chat_presetall(self, p, params):
		self.silent = True
		for weapon in list(self.modifiedWeapons):
			data = self.defaultValues(weapon)
			try:
				self.processData([weapon, data[0], data[1], str(data[2]), str(data[3])])
			except:
				p.sendMsg("ERROR - " + str([weapon, data[0], data[1], str(data[2]), str(data[3])]))
		self.silent = False
		self.modifiedWeapons = []
		self.sendMsg("All weapons resetted.")
 
	def chat_pinfo(self, p, params):
		weapon = None
		if len(params) > 0:
			weapon = self.getName(params[0], WEAPON_DATA)
			if not weapon:
				self.sendMsg("ERROR - Bad weapon name (低1001" + params[0] + "低1001).")
				return
		else:
			try: weapon = p.getPrimaryWeapon().templateName
			except:
				self.sendMsg("ERROR - No weapon selected.")
				return
		string = ["Projectile: ", "Velocity: ", "RPM: ", "Delay: "]
		gold = "低1001"
		finalString = "Weapon: " + gold + weapon + gold
		for i in range(0, 4):
			data = self.CURRENT_DATA[weapon][i]
			if data:
				finalString += " - " + string[i] + gold + data + gold
		self.sendMsg(finalString + ".")
 
	def chat_pactive(self, p, params):
		p.activeWeapon = params[0]
 
	def chat_pclearactive(self, p, params):
		p.activeWeapon = None
 
	def chat_pproj(self, p, params):
		if p.activeWeapon: host.rcon_invoke("ObjectTemplate.active " + p.activeWeapon)
		host.rcon_invoke("ObjectTemplate.projectileTemplate " + params[0])
 
	def chat_pspeed(self, p, params):
		if p.activeWeapon: host.rcon_invoke("ObjectTemplate.active " + p.activeWeapon)
		host.rcon_invoke("ObjectTemplate.velocity " + params[0])
 
	def chat_prpm(self, p, params):
		if p.activeWeapon: host.rcon_invoke("ObjectTemplate.active " + p.activeWeapon)
		host.rcon_invoke("ObjectTemplate.fire.roundsPerMinute " + params[0])
 
	def chat_pdelay(self, p, params):
		if p.activeWeapon: host.rcon_invoke("ObjectTemplate.active " + p.activeWeapon)
		host.rcon_invoke("ObjectTemplate.delayToUse " + params[0])
 
	def getName(self, name, list):
		name = name.lower()
		for i in list.keys():
			if name == i.lower(): return i
			for i2 in list[i]:
				if name == i2.lower(): return i
		return None
 
	def defaultValues(self, name):
		for i in DEFAULT_DATA:
			if i.lower() == name.lower():
				list = DEFAULT_DATA[i]
				return list
		return None
 
	def processData(self, params):
		weapon = params[0]
		params[0] = self.getName(params[0], WEAPON_DATA)
		params[1] = self.getName(params[1], PROJECTILE_DATA)
		if not params[0]:
			self.sendMsg("ERROR - Bad weapon name (低1001" + weapon + "低1001).")
			return
		newData = self.defaultValues(params[0])
		for i in range(1, 5):
			if len(params) >= (i + 1):
				if not params[i] or not newData[i - 1]: params[i] = newData[i - 1]
			else:
				params.append(newData[i - 1])
		self.invokeData(params)
 
	def invokeData(self, data):
		setting = ["ObjectTemplate.projectileTemplate", "ObjectTemplate.velocity", "ObjectTemplate.fire.roundsPerMinute", "ObjectTemplate.delayToUse"]
		string = ["Projectile: ", "Velocity: ", "RPM: ", "Delay: "]
		gold = "低1001"
		finalString = "Weapon: " + gold + data[0] + gold
		if data[0] not in self.CURRENT_DATA.keys():
			self.CURRENT_DATA[data[0]] = [None, None, None, None]
		host.rcon_invoke("ObjectTemplate.active " + str(data[0]))
		for i in range(1, 5):
			value = True
			if i > 1:
				try: data[i] = str(float(data[i]))
				except: value = False
			if value:
				if data[i] and data[i] != self.CURRENT_DATA[data[0]][i - 1]:
					host.rcon_invoke(setting[i - 1] + " " + str(data[i]))
					if data[0] not in self.modifiedWeapons: self.modifiedWeapons.append(data[0])
					finalString += " - " + string[i - 1] + gold + data[i] + gold
				self.CURRENT_DATA[data[0]][i - 1] = data[i]
		self.sendMsg(finalString + ".")
 
	def sendMsg(self, message):
		if not self.silent: self.core.sendMsg(message)