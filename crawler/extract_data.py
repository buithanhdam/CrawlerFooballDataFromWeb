
def extract_data_from_web(row_elements):
    import re
    list_leagues = []
    clubs = []
    matchs = []
    league = {}
    if row_elements:
        for row_element in row_elements:
            if row_element.find("th"):
                if len(league) != 0:
                    league.__setitem__("matchs", matchs)
                    list_leagues.append(league)
                    league = {}
                    matchs = []
                row_league_th_elements = row_element.find_all("th")
                league_element = row_league_th_elements[1]
                a_href_league_element = league_element.find("a").get("href")
                text_league_element = league_element.find("a").text
                text_tokens = text_league_element.split(" > ")
                league.__setitem__("region", text_tokens[0].strip() if text_tokens[0] != None else None)
                league.__setitem__("tournament", text_tokens[1].strip() if text_tokens[1] != None else None)
                if len(text_tokens) > 2:
                    league.__setitem__("matchday", text_tokens[2].strip())
                else:
                    league.__setitem__("matchday", None)
                league.__setitem__("league_href", a_href_league_element if a_href_league_element != None else None)
                league.__setitem__("matchs", [])
            elif row_element.find("td"):
                row_match_elements = row_element.find_all("td")
                first_match_element = row_match_elements[0]
                second_match_element = row_match_elements[1].find("a")
                third_match_element = row_match_elements[3].find("a")
                fourth_match_element = row_match_elements[4]
                match = {}
                begin_time = first_match_element.text
                first_team = second_match_element.text
                first_team_href = second_match_element.get("href")
                second_team = third_match_element.text
                second_team_href = third_match_element.get("href")
                full_match_goals = ""
                half_match_goals = ""
                first_team_goals = ""
                second_team_goals = ""
                match_href = ""

                def has_numbers(inputString):
                    return any(char.isdigit() for char in inputString)

                def transform_goals_line(inputString):
                    if not has_numbers(inputString):
                        return None, None, None, None
                    else:
                        str_tokens = inputString.split(" ")
                        str_tokens[0] = re.sub('\n', '', str_tokens[0])
                        fm = ""
                        hm = ""
                        goals_token = []
                        if len(str_tokens) > 2:
                            fm = str_tokens[0]
                            hm = str_tokens[1].strip("(").strip(")")
                            goals_token = fm.split(":")
                        else:
                            hm = None
                            fm = str_tokens[0]
                            goals_token = fm.split(":")
                        return fm, hm, goals_token[0], goals_token[1]

                if fourth_match_element.find("a"):
                    fa = fourth_match_element.find("a")
                    match_href = fa.get("href")
                    score_string = fa.text
                    full_match_goals, half_match_goals, first_team_goals, second_team_goals = transform_goals_line(
                        score_string)
                else:
                    match_href = None
                    score_string = fourth_match_element.text
                    full_match_goals, half_match_goals, first_team_goals, second_team_goals = transform_goals_line(
                        score_string)

                match.__setitem__("begin_time", begin_time)
                match.__setitem__("first_team", first_team)
                match.__setitem__("second_team", second_team)
                match.__setitem__("full_match_goals", full_match_goals)
                match.__setitem__("half_match_goals", half_match_goals)
                match.__setitem__("first_team_goals", first_team_goals)
                match.__setitem__("second_team_goals", second_team_goals)
                match.__setitem__("match_href", match_href)
                matchs.append(match)
                club1 = {"club_name": first_team, "club_href": first_team_href}
                club2 = {"club_name": second_team, "club_href": second_team_href}
                if not any(
                        club.get('name') == club1.get("club_name")
                        for club in clubs
                ):
                    clubs.append(club1)
                if not any(
                        club.get('name') == club2.get("club_name")
                        for club in clubs
                ):
                    clubs.append(club2)
        return list_leagues,clubs
    else:
        print("[ERROR]: Extract Erros: "+"Row elements is None")
        return None