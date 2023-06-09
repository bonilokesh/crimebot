from telegram import *
from telegram.ext import *




updater =Updater("5979422332:AAGL6IehysmtIOSCVkBB_HtgYpPAqcipvqE",use_context=True)
def start(update: Update,context:CallbackContext):
    update.message.reply_text("WELCOME! \nHERE YOU CAN START REGISTERING FOR A COMPLAINT. \nTO REGISTER CLICK /register \n FOR ANY HELP CLICK /help")
def help(update: Update,context: CallbackContext):
    update.message.reply_text(
        "TO GET MORE INFORMATION CONTACT TOLL-FREE NUMBER /6302414159" )
def register(update: Update,context:CallbackContext):
    update.message.reply_text("WHAT TYPE OF COMPLAINT YOU WANT TO REGISTER:\n1./MURDER\n2./CHAINSNATCHER\n3./MISSINGCOMPLAINT\n4./HARRASMENT\n5./LANDISSUES" )   
def murder(update:Update,context:CallbackContext):
     update.message.reply_text("CLICK ON THIS LINK TO REGISTER DETAILS -https://docs.google.com/forms/d/1nVENEzvMg2jkDM3o3n1xAdM5uafUfpTHywXqbmxV9wo/edit" )

def chainsnatcher(update: Update,context: CallbackContext):
    update.message.reply_text("CLICK ON THIS LINK TO REGISTER DETAILS -https://docs.google.com/forms/d/1eLahawuwsZ1TSQqUuIkXMF9RC-p9y8jsWxSnxEtJ9UM/edit")
   
def MISSINGCOMPLAINT(update: Update,context:CallbackContext):
    update.message.reply_text("CLICK ON THIS LINK TO REGISTER DETAILS -https://docs.google.com/forms/d/e/1FAIpQLScboX4Gf1U1B0RUpKOEPQAPRL17jVzYX92lvI_x9X80T-w6zA/viewform?usp=sf_link")   

def HARRASMENT(update: Update,context: CallbackContext):
    update.message.reply_text("CLICK ON THIS LINK TO REGISTER DETAILS -https://docs.google.com/forms/d/e/1FAIpQLSfdFF5HVVSTtFbipkR7bYJN7CF26XSx1SLSuOwnYCcTzw8daw/viewform?usp=sf_link")    
        
def LANDISSUES(update: Update, context: CallbackContext):
    update.message.reply_text("CLICK ON THIS LINK TO REGISTER DETAILS -https://docs.google.com/forms/d/e/1FAIpQLSf7AKVuCh2zdhMkcf6XPT3W8InwqNBPEu0LasQWBH2xTRS7GA/viewform?usp=sf_link")
       

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(CommandHandler('register',register))
updater.dispatcher.add_handler(CommandHandler("murder",murder))
updater.dispatcher.add_handler(CommandHandler("chainsnatcher",chainsnatcher))
updater.dispatcher.add_handler(CommandHandler("HARRASMENT",HARRASMENT))
updater.dispatcher.add_handler(CommandHandler("MISSINGCOMPLAINT",MISSINGCOMPLAINT))
updater.dispatcher.add_handler(CommandHandler("LANDISSUES",LANDISSUES))
updater.start_polling() 

