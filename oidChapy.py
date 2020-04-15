# oidChapie
# application python qui gè le CRUD des clefs de l'usager
# Créé le 14 avril 2020
# Révisé le: 15 avril 2020
#
# Les révisions sont faites dans le fichier \Users\Utilisateur\Progge\ChaPie\oidChapie.py
# Une copie dans F:\copiesSurEffeDeuPoin\oidChapie.py

import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkst
import re
import sqlite3
from tkinter import ttk

global print_enregistrements
global nom_site_color
global nom_site_txt
global ur_l_txt
global nom_utilisateur_txt
global cle_f_txt
global q_1_txt
global r_1_txt
global q_2_txt
global r_2_txt
global q_3_txt
global r_3_txt
global q_4_txt
global r_4_txt
global q_5_txt
global r_5_txt
global no_te_txt
global query_lbl
global lbl_aide
global lbl_non_utili
global query_lst
global query_info
global delete_box_txt
# global o_i_d
global total_index
global v_nom_utili
global n_utili
global n_ta_ble

root = tk.Tk()

root.title("Chapie perso")
root.geometry("1150x570")

v_nom_utili = StringVar()
query_info = tk.StringVar()


def fenet_aid_fr():
    root.geometry("1150x810")
    aide_info = "Lors de la première utilisation de l\'application ChaPy," \
                "\ndeux nouveaux fichiers ont été créés dans le même répertoire que l\'application:" \
                "\nsites_chapy.db et archiv_chapy.txt." \
                "\nCes fichiers doivent être laissés en place enregistrés inclus avec vos mises à jour" \
                "\n\nPour ajouter un enregistrement, inscrire les informations dans les champs de votre choix" \
                "\n(le champ URL est obligatoire)" \
                "et cliquer sur \"Ajouter aux sites\". " \
                "Ceci ajoute les données dans une table du fichier \"sites_chapy.db\"" \
                "\n\nPour chercher les informations, cliquer sur \"Recherche\", ou précisez des éléments de recherche" \
                "\ndans le champ \"URL\", ou \"Courriel\" ou \"Clé primaire\"" \
                "\n\nPour effacer un enregistrement, écrire le nom exact de l\'\"URL\" dans le champ correspondant" \
                "\net cliquer sur \"Archiver\". Les informations sont toutes conservées dans le fichier archiv_chapy.txt"
    lbl_aide = Label(root, bg="white")
    lbl_aide.config(text=aide_info, justify=LEFT)
    lbl_aide.grid(row=20, column=0, columnspan=4, sticky=W + E)

    # placer_lbl(query_info)


chapiConn = sqlite3.connect("sites_chapy.db")
c = chapiConn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS sites_oid_chapi(
        nom_site            TEXT,
        ur_l                TEXT    NOT NULL,
        nom_utilisateur     TEXT,
        cour_riel           TEXT,
        cle_f               TEXT,
        q_1                 TEXT,
        r_1                 TEXT,
        q_2                 TEXT,
        r_2                 TEXT,
        q_3                 TEXT,
        r_3                 TEXT,
        q_4                 TEXT,
        r_4                 TEXT,
        q_5                 TEXT,
        r_5                 TEXT,
        no_te               TEXT
        )
    """)
chapiConn.commit()
chapiConn.close()


def variab_nom(var_nom, ntabl):
    if var_nom == "":
        ntabl.destroy()
    else:
        query_info = "Utilisateur : " + var_nom
        placer_lbl(query_info)
        ntabl.destroy()


def prendrelenomparlapoinpoin():
    global texte_lbl_n
    global lbl_no
    global txt_n_utili
    n_utili = tk.StringVar()

    def only_members(ese):
        if re.search(r'[\w\-. ]', ese):
            return TRUE
        else:
            # lbl_no = Label(n_tabl, text="Pas ce caractère...", bg="yellow")
            lbl_no.grid_forget()
            query_lst.grid_forget()
            lbl_no.grid(row=0, column=2)
            return FALSE

    n_tabl = tk.Tk()
    n_tabl.title("Accueil")
    n_tabl.geometry("330x100")
    # nom_nouvel_utili = tk.StringVar()
    texte_lbl_n = tk.StringVar()
    texte_lbl_n = "Inscrire votre nom (lettres, chiffres, \"-\", \".\" ou espaces)"

    lbl_n_tabl = tk.Label(n_tabl, text=texte_lbl_n, anchor=W)
    lbl_n_tabl.grid(row=0, column=0, columnspan=2, padx=5, ipadx=5, ipady=5)
    valider_n_tabl = (n_tabl.register(only_members), '%S')
    txt_n_utili = tk.Entry(n_tabl, textvariable=n_utili, validate="key", vcmd=valider_n_tabl, width=50)
    txt_n_utili.grid(row=1, column=0, columnspan=2, ipadx=2, ipady=2)
    txt_n_utili.focus()
    cmd_creer_n_tabl = tk.Button(n_tabl, text="Créer", width=12, command=lambda: variab_nom(txt_n_utili.get(), n_tabl))
    cmd_creer_n_tabl.grid(row=2, column=0, ipady=2)
    cmd_annul_tabl = tk.Button(n_tabl, text="Annuler", width=12, command=n_tabl.destroy)
    cmd_annul_tabl.grid(row=2, column=1, ipady=2)


def placer_lbl(queri_info):
    lbl_non_utili.config(text=queri_info, justify=LEFT)
    # root.geometry("1200x570")
    lbl_non_utili.grid(row=18, column=1, columnspan=4, sticky=W+E)


def placer_lbl_ed(queri_info):
    editor.geometry("830x450")
    lbl_non_utili_ed.config(text=queri_info, justify=LEFT)
    lbl_non_utili_ed.grid(row=16, column=1, columnspan=3)


def comand_quitter():
    quiter_peutetre = tk.Tk()
    quiter_peutetre.title("")
    quiter_peutetre.config(bg="lightpink")
    quiter_peutetre.geometry("450x90")

    def go_quit():
        quiter_peutetre.destroy()
        root.destroy()

    lbl_quitter = tk.Label(quiter_peutetre, text='Voulez-vous arrêter le programme?'
                                                 '\nToutes les ajouts et modifications ont déjà été inscrits dans la base de données'
                                                 '\nlorsque vous avez appuyé sur le bouton"Ajouter à la base de donnée\" ou \"MAJ\"')
    lbl_quitter.config(bg="lightpink", justify=LEFT)
    lbl_quitter.pack()
    cmd_quitter = tk.Button(quiter_peutetre, text="Quitter", command=go_quit)
    cmd_quitter.pack()


menubar = tk.Menu(root)
fichier_menu = tk.Menu(menubar, tearoff=0)
fichier_menu.add_command(label="Nom de l\'utilisateur", command=prendrelenomparlapoinpoin)
fichier_menu.add_command(label="Quitter", command=comand_quitter)
menubar.add_cascade(label="Fichier", menu=fichier_menu)
aid_menu = tk.Menu(menubar, tearoff=0)
aid_menu.add_command(label="Informations", command=fenet_aid_fr)
menubar.add_cascade(label="Aide", menu=aid_menu)

nom_site_color = tk.StringVar()
total_index = 0

chapiConn = sqlite3.connect("sites_chapy.db")
c = chapiConn.cursor()


# <!------- ceci est le modelle de conditions
def submit():
    if ur_l_txt.get() != "" or delete_box_txt.get() == "":
        ur_l_txt.config(bg="white")
        # cour_riel_txt.config(bg="pink")
        if re.search(r'\w*\.?\w*\.?\w*\.?\w*\.[a-zA-Z]+$', ur_l_txt.get()) and re.search('[^@,]', ur_l_txt.get()):
            ur_l_txt.config(bg="white")
            if re.search(r'\w+@\w+\.\w+$', cour_riel_txt.get()) or cour_riel_txt.get() == "":
                inserer_chapy()
                info_confirmation = "Enregistrement de {} complété.".format(ur_l_txt.get())
                placer_lbl(info_confirmation)
                vider_champs()
            else:
                query_info = "Pour soumettre un courriel avec le site, le champ doit comprendre\n" \
                             " un caractère alpha-numériques ou plus,\n" \
                             "un \"@\") et un \".\"."
                placer_lbl(query_info)
                cour_riel_txt.config(bg="pink")
        else:
            query_info = "Pour soumettre un nouveau site,\nle champ \"Url\" comporte un point \".\"" \
                         "\nsuivi de caractères alpha-numériques (sauf \"@\")."
            placer_lbl(query_info)
            cour_riel_txt.config(bg="white")
            ur_l_txt.config(bg="pink")
    else:
        query_info = "Pour soumettre un nouveau site,\nle champ\"Url\" doit être rempli." \
                     "\nLes inscriptions du champ \"Clé primaire\" ne seront pas enregistrées )"
        placer_lbl(query_info)
        ur_l_txt.config(bg="pink")
    if delete_box_txt.get() != "":
        query_info = "Les inscriptions du champ \"Clé primaire\" ne seront pas enregistrées"
        placer_lbl(query_info)

    # chapiConn.commit()
    # chapiConn.close()


def inserer_chapy():
    chapiConn = sqlite3.connect("sites_chapy.db")
    c = chapiConn.cursor()
    # curle = c.fetchall()
    c.execute(
        "INSERT INTO sites_oid_chapi VALUES (:nom_site, :ur_l, :nom_utilisateur, :cour_riel, :cle_f, :q_1, :r_1, :q_2, :r_2, :q_3, :r_3, :q_4, :r_4, :q_5, :r_5, :no_te)",
        {
            'nom_site': nom_site_txt.get(),
            'ur_l': ur_l_txt.get(),
            'nom_utilisateur': nom_utilisateur_txt.get(),
            'cour_riel': cour_riel_txt.get(),
            'cle_f': cle_f_txt.get(),
            'q_1': q_1_txt.get(),
            'r_1': r_1_txt.get(),
            'q_2': q_2_txt.get(),
            'r_2': r_2_txt.get(),
            'q_3': q_3_txt.get(),
            'r_3': r_3_txt.get(),
            'q_4': q_4_txt.get(),
            'r_4': r_4_txt.get(),
            'q_5': q_5_txt.get(),
            'r_5': r_5_txt.get(),
            'no_te': no_te_txt.get()
        })
    #             'o_i_d': o_i_d,
    chapiConn.commit()
    c.close()
    chapiConn.close()
    # vider_champs()


def edit():
    chapiConn = sqlite3.connect("sites_chapy.db")
    c = chapiConn.cursor()
    cee = chapiConn.cursor()
    if delete_box_txt.get() != "":
        c.execute("SELECT oid from sites_oid_chapi")
        fetcher = c.fetchall()
        num_delete = delete_box_txt.get()
        lenne = int(delete_box_txt.get())
        if lenne <= len(fetcher):  # c.fetchall()):
            cee.execute("SELECT *, oid FROM sites_oid_chapi WHERE oid = '" + num_delete + "'")
            batir_editTk(cee.fetchall())

    elif ur_l_txt.get() != "":
        c.execute("SELECT ur_l FROM sites_oid_chapi")
        fetcher = c.fetchall()
        url_get = ur_l_txt.get()
        if (any(url_get in i for i in fetcher)):
            cee.execute("SELECT *, oid FROM sites_oid_chapi WHERE ur_l = '" + url_get + "'")
            batir_editTk(cee.fetchall())
    else:
        chapiConn.close()
        c.close()
        return


def batir_editTk(choi):  # choi = fetchall!!!
    global editor
    global nom_site_editor
    global ur_l_editor
    global nom_utilisateur_editor
    global cour_riel_editor
    global cle_f_editor
    global q_1_editor
    global r_1_editor
    global q_2_editor
    global r_2_editor
    global q_3_editor
    global r_3_editor
    global q_4_editor
    global r_4_editor
    global q_5_editor
    global r_5_editor
    global no_te_editor
    global delete_editor
    global lbl_non_utili_ed
    editor = tk.Tk()
    editor.title("Mise à jour de ...")
    editor.geometry("830x380")
    # conn = sqlite3.connect("sites_chapy.db")
    # cee = conn.cursor()
    # if delete_box_txt.get != "":
    #     cee.execute("SELECT * FROM sites_oid_chapi WHERE oid = '" + delete_box_txt.get() + "'")
    #
    # elif ur_l_txt.get() != "":
    #     cee.execute("SELECT * FROM sites_oid_chapi WHERE ur_l = '" + ur_l_txt.get() + "'")
    # else:
    #     return#
    # enregistrements = cee.fetchall()
    # enregistrements = choi
    nom_site_editor = tk.Entry(editor, width=50)
    nom_site_editor.grid(row=0, column=1)
    ur_l_editor = tk.Entry(editor, width=50)
    ur_l_editor.grid(row=1, column=1)
    nom_utilisateur_editor = tk.Entry(editor, width=50)
    nom_utilisateur_editor.grid(row=2, column=1)
    cour_riel_editor = tk.Entry(editor, width=50)
    cour_riel_editor.grid(row=3, column=1)
    cle_f_editor = tk.Entry(editor, width=50)
    cle_f_editor.grid(row=4, column=1)
    q_1_editor = tk.Entry(editor, width=50)
    q_1_editor.grid(row=5, column=1)
    r_1_editor = tk.Entry(editor, width=50)
    r_1_editor.grid(row=6, column=1)
    q_2_editor = tk.Entry(editor, width=50)
    q_2_editor.grid(row=7, column=1)
    r_2_editor = tk.Entry(editor, width=50)
    r_2_editor.grid(row=8, column=1)
    q_3_editor = tk.Entry(editor, width=50)
    q_3_editor.grid(row=9, column=1)
    r_3_editor = tk.Entry(editor, width=50)
    r_3_editor.grid(row=10, column=1)
    q_4_editor = tk.Entry(editor, width=50)
    q_4_editor.grid(row=11, column=1)
    r_4_editor = tk.Entry(editor, width=50)
    r_4_editor.grid(row=12, column=1)
    q_5_editor = tk.Entry(editor, width=50)
    q_5_editor.grid(row=13, column=1)
    r_5_editor = tk.Entry(editor, width=50)
    r_5_editor.grid(row=14, column=1)
    no_te_editor = tk.Entry(editor, width=50)
    no_te_editor.grid(row=15, column=1)
    delete_editor = tk.Entry(editor, width=50)
    delete_editor.grid(row=16, column=1)

    lbl_nom_site = tk.Label(editor, text=nom_site_v[0], width=30, anchor=tk.W)
    lbl_nom_site.grid(row=0, column=0)
    lbl_ur_l = tk.Label(editor, text=nom_site_v[1], width=30, anchor=tk.W)
    lbl_ur_l.grid(row=1, column=0)
    lbl_nom_utilisateur = tk.Label(editor, text=nom_site_v[2], width=30, anchor=tk.W)
    lbl_nom_utilisateur.grid(row=2, column=0, sticky=tk.W)
    lbl_cour_riel = tk.Label(editor, text=nom_site_v[3], width=30, anchor=tk.W)
    lbl_cour_riel.grid(row=3, column=0)
    lbl_cle_f = tk.Label(editor, text=nom_site_v[4], width=30, anchor=tk.W)
    lbl_cle_f.grid(row=4, column=0)
    lbl_q_1 = tk.Label(editor, text=nom_site_v[5], width=30, anchor=tk.W)
    lbl_q_1.grid(row=5, column=0)
    lbl_r_1 = tk.Label(editor, text=nom_site_v[6], width=30, anchor=tk.W)
    lbl_r_1.grid(row=6, column=0)
    lbl_q_2 = tk.Label(editor, text=nom_site_v[7], width=30, anchor=tk.W)
    lbl_q_2.grid(row=7, column=0)
    lbl_r_2 = tk.Label(editor, text=nom_site_v[8], width=30, anchor=tk.W)
    lbl_r_2.grid(row=8, column=0)
    lbl_q_3 = tk.Label(editor, text=nom_site_v[9], width=30, anchor=tk.W)
    lbl_q_3.grid(row=9, column=0)
    lbl_r_3 = tk.Label(editor, text=nom_site_v[10], width=30, anchor=tk.W)
    lbl_r_3.grid(row=10, column=0)
    lbl_q_4 = tk.Label(editor, text=nom_site_v[11], width=30, anchor=tk.W)
    lbl_q_4.grid(row=11, column=0)
    lbl_r_4 = tk.Label(editor, text=nom_site_v[12], width=30, anchor=tk.W)
    lbl_r_4.grid(row=12, column=0)
    lbl_q_5 = tk.Label(editor, text=nom_site_v[13], width=30, anchor=tk.W)
    lbl_q_5.grid(row=13, column=0)
    lbl_r_5 = tk.Label(editor, text=nom_site_v[14], width=30, anchor=tk.W)
    lbl_r_5.grid(row=14, column=0)
    lbl_no_te = tk.Label(editor, text=nom_site_v[15], width=30, anchor=tk.W)
    lbl_no_te.grid(row=15, column=0)
    lbl_delete_editor = tk.Label(editor, text=nom_site_v[16], width=30, anchor=tk.W)
    lbl_delete_editor.grid(row=16, column=0)
    query_info = ""
    lbl_non_utili_ed = Label(editor, text=query_info, bg="white")

    for enregisse in choi:  # enregistrements:
        nom_site_editor.insert(0, enregisse[0])
        ur_l_editor.insert(0, enregisse[1])
        nom_utilisateur_editor.insert(0, enregisse[2])
        cour_riel_editor.insert(0, enregisse[3])
        cle_f_editor.insert(0, enregisse[4])
        q_1_editor.insert(0, enregisse[5])
        r_1_editor.insert(0, enregisse[6])
        q_2_editor.insert(0, enregisse[7])
        r_2_editor.insert(0, enregisse[8])
        q_3_editor.insert(0, enregisse[9])
        r_3_editor.insert(0, enregisse[10])
        q_4_editor.insert(0, enregisse[11])
        r_4_editor.insert(0, enregisse[12])
        q_5_editor.insert(0, enregisse[13])
        r_5_editor.insert(0, enregisse[14])
        no_te_editor.insert(0, enregisse[15])
        delete_editor.insert(0, enregisse[16])  # delete_box_txt.get())#record_id)
        delete_editor.config(state=DISABLED)

    edit_btn = tk.Button(editor, text="Enregistrer ce changement", command=update)
    edit_btn.grid(row=0, column=2)


def update():
    #     # oid automatique?...:o_i_d,
    if ur_l_editor.get() != "":
        ur_l_editor.config(bg="white")
        if re.search(r'\w*\.?\w*\.?\w*\.?\w*\.[a-zA-Z]+$', ur_l_editor.get()) and re.search('[^@,]', ur_l_editor.get()):
            ur_l_editor.config(bg="white")
            chapiConnU = sqlite3.connect("sites_chapy.db")
            c = chapiConnU.cursor()
            record_id = delete_editor.get()
            c.execute("""UPDATE sites_oid_chapi SET
                nom_site = :nom_site,
                ur_l = :ur_l,
                nom_utilisateur = :nom_utilisateur,
                cour_riel = :cour_riel,
                cle_f = :cle_f,
                q_1 = :q_1,
                r_1 = :r_1,
                q_2 = :q_2,
                r_2 = :r_2,
                q_3 = :q_3,
                r_3 = :r_3,
                q_4 = :q_4,
                r_4 = :r_4,
                q_5 = :q_5,
                r_5 = :r_5,
                no_te = :no_te
        
                WHERE oid = :oid""",
                  {
                      'nom_site': nom_site_editor.get(),
                      'ur_l': ur_l_editor.get(),
                      'nom_utilisateur': nom_utilisateur_editor.get(),
                      'cour_riel': cour_riel_editor.get(),
                      'cle_f': cle_f_editor.get(),
                      'q_1': q_1_editor.get(),
                      'r_1': r_1_editor.get(),
                      'q_2': q_2_editor.get(),
                      'r_2': r_2_editor.get(),
                      'q_3': q_3_editor.get(),
                      'r_3': r_3_editor.get(),
                      'q_4': q_4_editor.get(),
                      'r_4': r_4_editor.get(),
                      'q_5': q_5_editor.get(),
                      'r_5': r_5_editor.get(),
                      'no_te': no_te_editor.get(),
                      'oid': record_id
                  })
            c.close()
            chapiConnU.commit()
            chapiConnU.close()  # <------prendre une chance
            query_info = "Modification {} complété".format(ur_l_editor.get())
            placer_lbl(query_info)
            editor.destroy()
        else:
            query_info = "Pour compléter la modification, assurez-vous que le champ URL comporte au minimum:" \
                         "\nau moins un caractère alpha-numériques (sauf \"@\")" \
                         "\nun point \".\"" \
                         "\nsuivi de caractères alpha-numériques (sauf \"@\")."
            placer_lbl_ed(query_info)

    else:
        editor.destroy()


def vider_champs():
    nom_site_txt.delete(0, tk.END)
    nom_site_txt.config(bg="white")
    ur_l_txt.delete(0, tk.END)
    ur_l_txt.config(bg="white")
    nom_utilisateur_txt.delete(0, tk.END)
    nom_utilisateur_txt.config(bg="white")
    cour_riel_txt.delete(0, tk.END)
    cour_riel_txt.config(bg="white")
    cle_f_txt.delete(0, tk.END)
    cle_f_txt.config(bg="white")
    q_1_txt.delete(0, tk.END)
    q_1_txt.config(bg="white")
    r_1_txt.delete(0, tk.END)
    r_1_txt.config(bg="white")
    q_2_txt.delete(0, tk.END)
    q_2_txt.config(bg="white")
    r_2_txt.delete(0, tk.END)
    r_2_txt.config(bg="white")
    q_3_txt.delete(0, tk.END)
    q_3_lbl.config(bg="white")
    r_3_txt.delete(0, tk.END)
    r_3_txt.config(bg="white")
    q_4_txt.delete(0, tk.END)
    q_4_lbl.config(bg="white")
    r_4_txt.delete(0, tk.END)
    r_4_lbl.config(bg="white")
    q_5_txt.delete(0, tk.END)
    q_5_lbl.config(bg="white")
    r_5_txt.delete(0, tk.END)
    r_5_lbl.config(bg="white")
    no_te_txt.delete(0, tk.END)
    no_te_txt.config(bg="White")
    delete_box_txt.delete(0, END)
    delete_box_txt.config(bg="White")
# def info_champs_vides():
#     ch_vid = [nom_site_txt, nom_utilisateur_txt, cle_f_txt, q_1_txt, r_2_txt, q_2_txt, r_2_txt, q_3_txt, r_3_txt,
#               q_4_txt, r_4_txt, q_5_txt, r_5_txt, no_te_txt]
#     # poir la version 1.2...
#     # info_v_c = str([i for i in ch_vid if i.get() == ""])
#     for i in ch_vid:
#         if i.get() == "":
#             query_info_v_c = "Si " + str(i)[:-4] + "_lbl ou plus de champs restent vides, l'opération est tout de même complétée avec succès"
#             break
#             placer_lbl(query_info_v_c)
# big shot sans ruban deroulant...			...pro chaine etape	<---------
def query():
    global tex_recherche
    tex_recherche = ""
    if ur_l_txt.get() != "":
        query_selon_champ("ur_l", ur_l_txt.get())
        vider_champs()
    elif cour_riel_txt.get() != "":
        query_selon_champ("cour_riel", cour_riel_txt.get())
        vider_champs()
    elif delete_box_txt.get() != "":
        query_selon_champ("oid", delete_box_txt.get())
        vider_champs()
    else:
        query_poin_all()


def query_poin_all():
    # global tex_recherche
    chapiConn = sqlite3.connect("sites_chapy.db")
    c = chapiConn.cursor()
    c.execute("SELECT *, oid FROM sites_oid_chapi")
    cee_fetch = c.fetchall()
    cee = ''
    for rowe in cee_fetch:
        if rowe[0]:
            cee += "\nNom du site : " + rowe[0] + "\n"
        cee += "URL : " + rowe[1] + "\n"
        if rowe[2]:
            cee += "Nom d\'utilisateur : " + rowe[2] + "\n"
        cee += "Courriel : " + rowe[3] + "\n"
        if rowe[4]:
            cee += "Clef : " + rowe[4] + "\n"
        if rowe[5]:
            cee += rowe[5] + "\n"
        if rowe[6]:
            cee += rowe[6]
        if rowe[7]:
            cee += rowe[7] + "\n"
        if rowe[8]:
            cee += rowe[8]
        if rowe[9]:
            cee += rowe[9] + "\n"
        if rowe[10]:
            cee += rowe[10]
        if rowe[11]:
            cee += rowe[11] + "\n"
        if rowe[12]:
            cee += rowe[12]
        if rowe[13]:
            cee += rowe[13] + "\n"
        if rowe[14]:
            cee += rowe[14]
        if rowe[15]:
            cee += rowe[15] + "\n"
        cee += "Clé primaire : " + str(rowe[16])
        cee += "\n///\\\\\\\n"
    # for choi in range(len(cee_fetch)):
    #     cee += "Gooooo" + "\n"
    tex_recherche = "Tous les sites :\n" + cee

    show_recherche(tex_recherche)  # , cee_fetch)
    chapiConn.commit()
    chapiConn.close()


def query_selon_champ(information, info_txt):
    # global tex_recherche
    chapiConn = sqlite3.connect("sites_chapy.db")
    c = chapiConn.cursor()
    c.execute("SELECT * , oid FROM sites_oid_chapi WHERE " + information + " LIKE '%" + info_txt + "%'")
    cee_fetch = c.fetchall()
    cee = ''
    for rowe in cee_fetch:
        if rowe[0]:
            cee += "Nom du site :\t" + rowe[0] + "\n"
        cee += "URL : " + rowe[1] + "\n"
        if rowe[2]:
            cee += "Nom d\'utilisateur :\t" + rowe[2] + "\n"
        cee += "Courriel : " + rowe[3] + "\n"
        if rowe[4]:
            cee += "Clef :\t" + rowe[4] + "\n"
        if rowe[5]:
            cee += "Question :\t" + rowe[5] + "\n"
        if rowe[6]:
            cee += "Réponse :\t" + rowe[6] + "\n"
        if rowe[7]:
            cee += "Question :\t" + rowe[7] + "\n"
        if rowe[8]:
            cee += "Réponse :\t" + rowe[8] + "\n"
        if rowe[9]:
            cee += "Question:\t" + rowe[9] + "\n"
        if rowe[10]:
            cee += "Réponse :\t" + rowe[10] + "\n"
        if rowe[11]:
            cee += "Question :\t" + rowe[11] + "\n"
        if rowe[12]:
            cee += "Réponse :\t" + rowe[12] + "\n"
        if rowe[13]:
            cee += "Question :\t" + rowe[13] + "\n"
        if rowe[14]:
            cee += "Réponse\t" + rowe[14] + "\n"
        if rowe[15]:
            cee += "Note :\t" + rowe[15] + "\n\n"
        cee += "Clé primaire : " + str(rowe[16])
        cee += "\n///\\\\\\\n"
    # for choi in range(len(cee_fetch)):
    #     cee += "Gooooo" + "\n"
    tex_recherche = "Selon les lettres clef :\n\n" + cee

    show_recherche(tex_recherche)  # , cee_fetch)
    chapiConn.commit()
    chapiConn.close()


def show_recherche(texx_rech):  # , c_fetche):
    montrer_clef = tkst.ScrolledText(root, undo=TRUE, width=70, height=10)
    montrer_clef.grid_forget()
    montrer_clef['font'] = ('Times', 9)
    montrer_clef.grid(row=0, column=2, rowspan=5, columnspan=2, padx=10, pady=(14, 0))
    montrer_clef.insert(END, texx_rech)


def archivedonc():
    chapiConn = sqlite3.connect("sites_chapy.db")
    c = chapiConn.cursor()
    if ur_l_txt.get() == "":
        archiv_info = "Aucun enregistrement n\'a été sélectionné dans le champ \"URL\"," \
                      "\nrien ne sera transféré à l\'archivage"
        placer_lbl(archiv_info)
    elif delete_box_txt.get() == "":
        archiv_info = "Aucun enregistrement n\'a été sélectionné dans le champ \"Clé\"," \
                      "\nrien ne sera transféré à l\'archivage." \
                      "\nLes références aux clés se trouvent selon le bouton recherche"
        placer_lbl(archiv_info)
    else:
        record_id = delete_box_txt.get()
        if delete_box_txt.get():
            c.execute("SELECT * FROM sites_oid_chapi WHERE oid = " + record_id)
        elif ur_l_txt.get():
            c.execute("SELECT * FROM sites_oid_chapi WHERE ur_l = " + ur_l_txt.get())
        # See = c.fetchall()
        with open('archiv_chapy.txt', 'a', encoding='utf-8') as archivChapi:
            cc = chapiConn.cursor()
            cc.execute("SELECT * FROM sites_oid_chapi WHERE oid = " + record_id)
            archivSelect = cc.fetchall()
            archivStr = str(archivSelect) + "\n"
            archivChapi.write(archivStr)
        c.execute("DELETE FROM sites_oid_chapi WHERE oid = " + record_id)  # cger delete_box_txt par recherche precise

        placer_lbl("Les données du document\n" + record_id + "\nont été archivé dans le document archivChapie.txt")
        vider_champs()
    chapiConn.commit()
    chapiConn.close()


# <!--lbl et Entry, etc.---!>
nom_site_v = ["Nom du site : ", "URL (Recherche ou Ajout) : ", "Nom d'utilisateur : ", "Courriel utilisé (Recherche): ",
              "Clef : ",
              "Question 1 : ", "Réponse (1) : ", "Question 2 : ", "Réponse (2) : ", "Question 3 : ", "Réponse (3) : ",
              "Question 4 : ", "Réponse (4) : ", "Question 5 : ", "Réponse (5) : ", "Note : ",
              "Clé primaire\n( pour mise à jour ou suppression)"]
nom_site_color = "white"

nom_site_lbl = tk.Label(root, text=nom_site_v[0], width=22, anchor=tk.W)
nom_site_lbl.grid(row=0, column=0, padx=10, pady=10)
nom_site_tkstring = tk.StringVar()
nom_site_lbl.config(bg=nom_site_color)
# nom_site_tkstring = ""
nom_site_txt = tk.Entry(root, textvariable=nom_site_tkstring, width=60, bg=nom_site_color)
nom_site_txt.grid(row=0, column=1, padx=10, pady=10)

ur_l_lbl = tk.Label(root, text=nom_site_v[1], width=22, anchor=tk.W)
ur_l_lbl.grid(row=1, column=0, padx=10, pady=10)
ur_l_lbl.config(bg=nom_site_color)
ur_l_tkstring = tk.StringVar()
ur_l_txt = tk.Entry(root, textvariable=ur_l_tkstring, width=60, bg=nom_site_color)
ur_l_txt.grid(row=1, column=1, padx=10, pady=10)

nom_utilisateur_lbl = tk.Label(root, text=nom_site_v[2], width=22, anchor=tk.W)
nom_utilisateur_lbl.grid(row=2, column=0, padx=10, pady=10)
nom_utilisateur_lbl.config(bg=nom_site_color)
nom_utilisateur_txt = tk.Entry(root, width=60)
nom_utilisateur_txt.grid(row=2, column=1, padx=10, pady=10)

cour_riel_lbl = tk.Label(root, text=nom_site_v[3], width=22, anchor=tk.W)
cour_riel_lbl.grid(row=3, column=0, padx=10, pady=10)
cour_riel_lbl.config(bg=nom_site_color)
cour_riel_tkstring = tk.StringVar()
cour_riel_txt = tk.Entry(root, textvariable=cour_riel_tkstring, width=60)
cour_riel_txt.grid(row=3, column=1, padx=10, pady=10)

cle_f_lbl = tk.Label(root, text=nom_site_v[4], width=22, anchor=tk.W)
cle_f_lbl.grid(row=4, column=0, padx=10, pady=10)
cle_f_lbl.config(bg=nom_site_color)
cle_f_txt = tk.Entry(root, width=60)
cle_f_txt.grid(row=4, column=1, padx=10, pady=10)

q_1_lbl = tk.Label(root, text=nom_site_v[5], width=22, anchor=tk.W)
q_1_lbl.grid(row=5, column=0, padx=10, pady=10)
q_1_lbl.config(bg=nom_site_color)
q_1_txt = tk.Entry(root, width=60)
q_1_txt.grid(row=5, column=1, padx=10, pady=10)

r_1_lbl = tk.Label(root, text=nom_site_v[6], width=22, anchor=tk.W)
r_1_lbl.grid(row=5, column=2, padx=10, pady=10)
r_1_lbl.config(bg=nom_site_color)
r_1_txt = tk.Entry(root, width=60)
r_1_txt.grid(row=5, column=3, padx=10, pady=10)

q_2_lbl = tk.Label(root, text=nom_site_v[7], width=22, anchor=tk.W)
q_2_lbl.grid(row=6, column=0, padx=10, pady=10)
q_2_lbl.config(bg=nom_site_color)
q_2_txt = tk.Entry(root, width=60)
q_2_txt.grid(row=6, column=1, padx=10, pady=10)

r_2_lbl = tk.Label(root, text=nom_site_v[8], width=22, anchor=tk.W)
r_2_lbl.grid(row=6, column=2, padx=10, pady=10)
r_2_lbl.config(bg=nom_site_color)
r_2_txt = tk.Entry(root, width=60)
r_2_txt.grid(row=6, column=3, padx=10, pady=10)

q_3_lbl = tk.Label(root, text=nom_site_v[9], width=22, anchor=tk.W)
q_3_lbl.grid(row=7, column=0, padx=10, pady=10)
q_3_lbl.config(bg=nom_site_color)
q_3_txt = tk.Entry(root, width=60)
q_3_txt.grid(row=7, column=1, padx=10, pady=10)

r_3_lbl = tk.Label(root, text=nom_site_v[10], width=22, anchor=tk.W)
r_3_lbl.grid(row=7, column=2, padx=10, pady=10)
r_3_lbl.config(bg=nom_site_color)
r_3_txt = tk.Entry(root, width=60)
r_3_txt.grid(row=7, column=3, padx=10, pady=10)

q_4_lbl = tk.Label(root, text=nom_site_v[11], width=22, anchor=tk.W)
q_4_lbl.grid(row=8, column=0, padx=10, pady=10)
q_4_lbl.config(bg=nom_site_color)
q_4_txt = tk.Entry(root, width=60)
q_4_txt.grid(row=8, column=1, padx=10, pady=10)

r_4_lbl = tk.Label(root, text=nom_site_v[12], width=22, anchor=tk.W)
r_4_lbl.grid(row=8, column=2, padx=10, pady=10)
r_4_lbl.config(bg=nom_site_color)
r_4_txt = tk.Entry(root, width=60)
r_4_txt.grid(row=8, column=3, padx=10, pady=10)

q_5_lbl = tk.Label(root, text=nom_site_v[13], width=22, anchor=tk.W)
q_5_lbl.grid(row=9, column=0, padx=10, pady=10)
q_5_lbl.config(bg=nom_site_color)
q_5_txt = tk.Entry(root, width=60)
q_5_txt.grid(row=9, column=1, padx=10, pady=10)

r_5_lbl = tk.Label(root, text=nom_site_v[14], width=22, anchor=tk.W)
r_5_lbl.grid(row=9, column=2, padx=10, pady=10)
r_5_lbl.config(bg=nom_site_color)
r_5_txt = tk.Entry(root, width=60)
r_5_txt.grid(row=9, column=3, padx=10, pady=10)

no_te_lbl = tk.Label(root, text=nom_site_v[15], width=22, anchor=tk.W)
no_te_lbl.grid(row=10, column=0, pady=(10, 0))
no_te_lbl.config(bg="white")
no_te_txt = tk.Entry(root, width=60)
no_te_txt.grid(row=10, column=1, pady=(10, 0))

delete_lbl = tk.Label(root, text=nom_site_v[16], width=30, anchor=tk.W)
delete_lbl.grid(row=10, column=2, rowspan=2, pady=(10, 0))
delete_lbl.config(bg="pink")
delete_box_txt = tk.Entry(root, width=60)
delete_box_txt.grid(row=10, column=3, pady=(10, 0))

# -------->validation youppi<-------------------------------
# def only_members(S):
#     if S.isdigit():
#         return TRUE
#     return FALSE
# delete_box_lbl = tk.Label(root, text="Pour une investigation... :", width=30, anchor=tk.W).grid(row=11, column=0, pady=(10, 0))
# valider_cmd = (root.register(only_members), '%S')                 <----utilie*******
# delete_box_txt = tk.Entry(root, validate="key", vcmd=valider_cmd, width=50)
# delete_box_txt.grid(row=11, column=1, pady=(10, 0))
# -------->validation youppi<-------------------------------
# valider_cmd = (root.register(only_members), '%S')                 <----utilie*******

kit_btn = tk.Frame(root, width=20, height=10)
kit_btn.grid(row=18, column=0, pady=5)

submit_cmd = tk.Button(kit_btn, text="Ajouter aux sites", command=submit, height=1, width=20).grid(row=12, column=0)
#                       -------------> changera par menu déroulant <---------
query_cmd = tk.Button(kit_btn, text="Recherche", command=query, width=20, height=1).grid(row=13, column=0)

#           ----> sera agrémenté d'une fonction d'archive <----------
del_cmd = tk.Button(kit_btn, text="Archiver", command=archivedonc, width=20, height=1).grid(row=14, column=0)
maj_cmd = tk.Button(kit_btn, text="Mise à jour", command=edit, width=20, height=1).grid(row=15, column=0)
query_lst = tk.Label(root, text=query_info, bg="white")  # textvariable=queri_info, bg="white")
query_info = "Commencez une recherche ou inscrivez un nouveau site\n" \
             "Le champ \"URL\" est obligatoire"
lbl_non_utili = Label(root, text=query_info, bg="white")
placer_lbl(query_info)

# def lbelle():
#     chapiConn = sqlite3.connect("sites_chapy.db")
#     c = chapiConn.cursor()
#     c.fetchall()
#     compte_chapi = tk.StringVar()
#     compte_chapi = c.execute("SELECT COUNT() FROM sites_oid_chapi")
#
#     chapiConn.commit()
#     chapiConn.close()
chapiConn.commit()
chapiConn.close()

root.config(bg="white", menu=menubar)
root.mainloop()