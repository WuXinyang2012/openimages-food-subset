import csv
import os, sys

dir = sys.path[0]
tmp_dir = dir + "/food/"
tmp = []
CLASS_LIST = ("/m/02wbm", "/m/01_bhs","/m/01b9xk","/m/02y6n","/m/01dwsz", "/m/01dwwc","/m/01j3zr","/m/01ww8y","/m/01f91_",
			 "/m/01hrv5", "/m/021mn","/m/0270h", "/m/01tcjp","/m/021mn","/m/0cxn2","/m/0fszt","/m/0gm28",
			 "/m/02g30s", "/m/02xwb","/m/014j1m","/m/0388q", "/m/043nyj","/m/061_f", "/m/07fbm7", "/m/07j87",
			 "/m/09k_b", "/m/09qck", "/m/0cyhj_","/m/0dj6p","/m/0fldg", "/m/0fp6w","/m/0hqkz","/m/0jwn_","/m/0kpqd",
			 "/m/0kpt_", "/m/033cnk","/m/052lwg6", "/m/01f91_","/m/01fb_0","/m/01tcjp", "/m/021mn","/m/09728",
			 "/m/0hnyx","/m/0jy4k", "/m/015wgc","/m/02zvsm","/m/052sf", "/m/05z55","/m/0663v", "/m/06nwz","/m/09gys",
			  "/m/0fbdv","/m/0_cp5", "/m/0cjq5","/m/0ll1f78", "/m/0n28_","/m/07crc", "/m/07mcwg","/m/0f4s2w","/m/015x4r",
			  "/m/015x5n","/m/047v4b", "/m/05vtc","/m/07j87","/m/0cjs7","/m/0dv77","/m/05zsy","/m/027pcv", "/m/0fbw6","/m/0fj52s",
			  "/m/0grw1","/m/0hkxq", "/m/0jg57","/m/02cvgx","/m/0fz0h", "/m/0l515","/m/0cdn1", "/m/06pcq","/m/0284d", "/m/01nkt",
			  "/m/04zpv","/m/07030" )

with open(dir + '/validation-annotations-bbox.csv', newline='') as csvfile:
	bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
	for bbox in bboxs:
		if bbox[0] == tmp:
			continue #Avoid downloading one image many times for the image which contains multiple target classes
		if bbox[2] in CLASS_LIST:
			tmp = bbox[0]
			os.system("gsutil cp gs://open-images-dataset/validation/%s.jpg %s"%(bbox[0], tmp_dir))
