# These are just some CSS selectors.
# I put them in classes and variables because it makes the code look better.


class Login:
    username = "#ctl00_ContentPlaceHolder_UserNameTextBox"
    password = "#ctl00_ContentPlaceHolder_PasswordTextBox"
    button = "#ctl00_ContentPlaceHolder_LoginButton"


class TrackHours:
    date = "#ctl00_ContentPlaceHolder_txtFrom"
    project = "#ctl00_ContentPlaceHolder_idProyectoDropDownList"
    hours = "#ctl00_ContentPlaceHolder_TiempoTextBox"
    assignment_type = "#ctl00_ContentPlaceHolder_idTipoAsignacionDropDownList"
    software_assignment = "#ctl00_ContentPlaceHolder_idTipoAsignacionDropDownList > option:nth-child(29)"
    description = "#ctl00_ContentPlaceHolder_DescripcionTextBox"
    focal_point = "#ctl00_ContentPlaceHolder_idFocalPointClientDropDownList"
    accept_button = "#ctl00_ContentPlaceHolder_btnAceptar"
