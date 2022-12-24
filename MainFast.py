
import gameshop.sign_user as sign_user
import gameshop.userpage as usergame
credentials = sign_user.login("rimexe", "1111")
usergame.Userpage.user_page(credentials)