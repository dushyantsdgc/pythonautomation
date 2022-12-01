@pytestrail.case('34672')
def test_that_IS_Admin_is_able_to_see_the_documents_posted_for_the_funds_and_investors_based_of_the_assigned_Domains(
        self):
    self.lp = LoginPage(self.driver)
    homePage = self.lp.do_login(ReadConfig.getusername("vf", "isadmin"),
                                ReadConfig.getpassword("vf", "isadmin"))
    time.sleep(3)

    vFundsLandingPage = homePage.do_click_vistra_application_icon()
    time.sleep(3)

    vFundsLandingPage.do_click_link_clients()
    client_name_for_search = ReadConfig.getclientnameforsearch()
    vFundsLandingPage.do_search(client_name_for_search)
    vFundsLandingPage.do_hover_table_funddashboards_first_row()
    vFundsLandingPage.do_click_table_funddashboards_first_row_button_details()
    assert vFundsLandingPage.is_label_fundsadministered_visible()

    administeredfundname = vFundsLandingPage.get_list_fundsadministeredfirstvalue_text()
    vFundsLandingPage.do_click_link_clients_funds()
    fund = (administeredfundname.split(" - ", 1)[0]).strip()
    vFundsLandingPage.do_search(fund)
    vFundsLandingPage.do_hover_table_funddashboards_first_row()
    vFundsLandingPage.do_click_table_funddashboards_first_row_button_details()
    sourcesystem = vFundsLandingPage.get_value_sourcesystem_text().strip().upper()
    assert "INVESTRAN" == sourcesystem
    fundid = vFundsLandingPage.get_value_yourinternalfundid_text()

    vFundsLandingPage.do_click_link_clients_investors()
    vFundsLandingPage.do_search((administeredfundname.split(" - ", 1)[0]).strip())
    investor = vFundsLandingPage.get_value_clients_investors_text()
    vFundsLandingPage.do_hover_table_funddashboards_first_row()
    vFundsLandingPage.do_click_table_funddashboards_first_row_button_details()
    # investorid = vFundsLandingPage.get_value_yourinternalid_text(vFundsLandingPage.value_yourinternalid_SuperAdminLoggedin_xpath)
    investorid = vFundsLandingPage.get_value_yourinternalid_text()
    dtn = datetime.now()
    currentdate = dtn.strftime('%m-%d-%Y-%H%M%S')
    # correspondencetype_list = ["Capital Call", "Distribution Notice", "Quarterly Reports", "Audited Financial Statements", "Legal", "Tax", "Annual Meeting", "Stock Distribution", "Unaudited Financial Statements", "Investment Advisor Reports", "Year End Letters"]
    correspondencetype_list = ["Capital Call"]
    currentdate1 = dtn.strftime('%Y-%m-%d-%H%M%S')
    investor_level_doc = correspondencetype_list[0] + " - " + currentdate1[:10] + " - " + "invtlevel" + currentdate1[
                                                                                                        11:]
    fund_level_doc = correspondencetype_list[0] + " - " + currentdate1[:10] + " - " + "fundlevel" + currentdate1[11:]

    for c_type in correspondencetype_list:
        investor_level_document_name = fundid + "_" + investorid + "_" + c_type + "_" + currentdate[
                                                                                        :10] + "_" + "invtlevel" + currentdate[
                                                                                                                   11:] + ".pdf"
        fund_level_document_name = fundid + "__" + c_type + "_" + currentdate[:10] + "_" + "fundlevel" + currentdate[
                                                                                                         11:] + ".pdf"
        docname_list = [investor_level_document_name, fund_level_document_name]

        for docname in docname_list:
            vFundsLandingPage.do_click_link_documents()
            pyautogui.FAILSAFE = False
            pyautogui.moveTo(100, 200)
            vFundsLandingPage.do_click_tab_documents_import()
            two_directory_up_path = os.path.abspath(os.path.join(__file__, "../"))
            pdf_path = os.path.abspath(os.path.join(two_directory_up_path, 'DocumentUplodToolTests', 'Data', "*.pdf"))
            file_list = glob.glob(pdf_path)
            oldname_pdf = os.path.abspath(
                os.path.join(two_directory_up_path, 'DocumentUplodToolTests', 'Data', file_list[0]))
            newname_pdf = os.path.abspath(
                os.path.join(two_directory_up_path, 'DocumentUplodToolTests', 'Data', docname))
            os.rename(oldname_pdf, newname_pdf)
            vFundsLandingPage.do_click_button_documents_import_browseyourcomputer()
            if vFundsLandingPage.driver.capabilities["browserName"] != "chrome":
                time.sleep(45)
            else:
                time.sleep(45)
            pyautogui.write(newname_pdf)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            vFundsLandingPage.do_scroll_table_documents_import()
            vFundsLandingPage.do_click_button_documents_upload_action_chains()
            time.sleep(3)
            str_uploaded = vFundsLandingPage.get_element_text_label_documents_import_status_uploaded()
            assert "uploaded" == str_uploaded.lower().strip(), "Document upload failed, UPLOADED string not appearing."

    pyautogui.FAILSAFE = True
    vFundsLandingPage.do_click_tab_documents_batches()
    assert vFundsLandingPage.is_label_documents_batches_visible()

    # search_string = fundid + dtn.strftime("-%Y-%m-%d")
    search_string = fundid + dtn.strftime("-%Y-%m")
    vFundsLandingPage.do_search(search_string)
    vFundsLandingPage.do_click_table_batchesdashboard_first_row_link_batch_name()
    # vFundsLandingPage.select_dropdown_value_documents_files_domainname()
    time.sleep(3)
    assert vFundsLandingPage.is_label_documents_files_visible()

    if vFundsLandingPage.is_indicator_online_file_visible():
        vFundsLandingPage.do_click_checkbox_filesdashboard_first_row()
        vFundsLandingPage.do_click_button_files_changestatus()
        vFundsLandingPage.do_click_field_files_changestatus_takeoffline()

    assert vFundsLandingPage.is_indicator_offline_file_visible(), "File offline indicator not appearing."

    vFundsLandingPage.do_click_checkbox_filesdashboard_first_row()
    status_changed_file_name = vFundsLandingPage.do_click_button_files_changestatus()
    assert vFundsLandingPage.is_changestatus_fields_visible(), "Change Status fields not appearing."

    vFundsLandingPage.do_click_field_files_changestatus_makeavailable()
    assert vFundsLandingPage.is_indicator_online_file_visible()

    vFundsLandingPage.do_click_tab_documents_folders()
    assert vFundsLandingPage.is_documents_folders_dashboard_client_xpath_visible()

    vFundsLandingPage.do_click_documents_folders_dashboard_client()
    fundnamewithid = fund + " - " + fundid
    assert vFundsLandingPage.is_visible_documents_folders_dashboard_client_fundwithid(fundnamewithid)

    vFundsLandingPage.do_click_documents_folders_dashboard_client_fundwithid(fundnamewithid)
    assert vFundsLandingPage.validate_the_folders_created_exist_in_appearing_folders_list(
        correspondencetype_list), "The expected correspondence type folder not appeared."

    vFundsLandingPage.do_click_link_documents_folders_capitalcall()
    assert vFundsLandingPage.validate_the_uploaded_doc_exist_in_appearing_docs_list(
        fund_level_doc), "The uploaded fund level document not appeared amongst fund level documents."

    vFundsLandingPage.do_click_link_documents_folders_capitalcall_fund()
    assert vFundsLandingPage.validate_the_uploaded_doc_exist_in_appearing_docs_list(
        investor_level_doc), "The uploaded investor level document not appeared amongst investor level documents."

    assert vFundsLandingPage.validate_the_changed_status_of_file_appears(status_changed_file_name, fund,
                                                                         fundid), "The online status is not appearing."
