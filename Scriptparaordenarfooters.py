from bs4 import BeautifulSoup
import os

# define the directory where the HTML files are located
directory = 'C:/Users/billg/Desktop/Esquivel opticas backup'

# define the new footer content
new_footer = '<footer class="section-p1">    <div class="col"> <img src="imagenes/Logo_Esquivel_Fondoblanco.png" width="180" height="100"  alt=""><p><strong>Dirección:</strong> Jr. Lanzon 295, San Juan de Lurigancho</p><p><strong>Telefono:</strong> +51 955 529 674</p><p><strong>Correo:</strong> ventas@esquivelopticas.com</p><p><strong>Horas de atención:</strong> 10:00 am - 18:00 pm </p><div class="follow"></div><div class="col"><h4>Acerca de nosotros</h4><a href="#">Informacion de delivery</a><a href="#">Politica de privacidad</a><a href="#">Terminos y condiciones</a><a href="#">Contactanos</a>             </div><div class="col"><h4>Siguenos</h4><div class="icon"><a class="fab fa-facebook"  href="https://www.facebook.com/esquivelopticas"></a>                    <a class="fab fa-instagram" href="https://www.instagram.com/esquivelopticas/"></a><a class="fab fa-whatsapp" href="https://wa.me/51955529674" ></a></div></div><!-- <div class="col"><h4>Mi cuenta</h4><a href="#">Ingresa</a><a href="#">Ver carro de compras</a><a href="#">Ayuda</a></div>--><!--   <div class="col install"><h4>Install app</h4><p>From app store or google play</p><div class="row"><img src="imagenes/225x125.png" alt=""><img src="imagenes/225x125.png" alt="">                 </div><p>Secured Payment Gateways</p><img src="imagenes/225x100.png" alt=""></div>--><div class="copyright"><p>© 2022, Esquivel Opticas - Distribucion de productos opticos</p></div></footer>'

# loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        # read the contents of the file
        with open(os.path.join(directory, filename), 'r') as file:
            contents = file.read()
        
        # parse the HTML using BeautifulSoup
        soup = BeautifulSoup(contents, 'html.parser')
        
        # find the existing footer element and replace its contents
        footer = soup.find('footer')
        footer.string = new_footer
        
        # write the modified HTML back to the file
        with open(os.path.join(directory, filename), 'w') as file:
            file.write(str(soup))