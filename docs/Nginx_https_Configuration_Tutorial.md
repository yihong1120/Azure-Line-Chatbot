Sure! Here's a tutorial on how to set up Nginx with HTTPS using Let's Encrypt in Markdown format:

# Nginx Tutorial: Setting up HTTPS with Let's Encrypt

In this tutorial, we will guide you through the process of setting up HTTPS for your Nginx server using Let's Encrypt. We will also configure Nginx to redirect HTTP traffic on ports 80 and 443 to HTTPS.

## Prerequisites

Before we begin, make sure you have the following:

- Ubuntu 20.04 server
- Access to a terminal window or command line
- Sudo or root privileges on your server
- Nginx installed and configured
- A registered domain name

## Step 1: Install Certbot

The first step is to install Certbot, an open-source software tool for automatically enabling HTTPS using Let's Encrypt certificates. Open a terminal window and run the following commands:

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

## Step 2: Check Nginx Configuration

Make sure you have a registered domain and an Nginx server block for that domain. Open the Nginx configuration file using a text editor:

```bash
sudo nano /etc/nginx/sites-available/example.com
```

Locate the `server_name` directive and ensure it is set to your domain name. For example:

```
server_name example.com www.example.com;
```

Save the file and check the Nginx configuration syntax:

```bash
sudo nginx -t
```

If there are no errors, reload the Nginx service:

```bash
sudo systemctl reload nginx
```

## Step 3: Adjust Firewall to Allow HTTPS Traffic

To allow HTTPS traffic, you need to adjust the firewall settings. Run the following command to check the firewall status:

```bash
sudo ufw status
```

If the firewall is active, you can either add the Nginx HTTPS profile or use Nginx Full and remove the existing Nginx HTTP rule. For example:

```bash
sudo ufw allow 'Nginx HTTPS'
sudo ufw deny 'Nginx HTTP'
sudo ufw allow 'Nginx Full'
```

Verify that the firewall rules are set correctly:

```bash
sudo ufw status
```

## Step 4: Obtain the SSL/TLS Certificate

Now, it's time to obtain the SSL/TLS certificate from Let's Encrypt. Run the following command:

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

Follow the prompts to configure your HTTPS settings, enter your email address, and agree to the terms of service. Certbot will generate the certificate and reload Nginx with the new settings.

Once the process is complete, Certbot will display the location of the certificate on your server.

## Step 5: Enable Automatic Certificate Renewal

Let's Encrypt certificates expire every 90 days, so it's important to set up automatic renewal. Open the crontab configuration file:

```bash
crontab -e
```

Add the following cron job to run the Certbot command daily at a specified time (e.g., 5:00 AM):

```
0 5 * * * /usr/bin/certbot renew --quiet
```

Save the file and exit.

Congratulations! You have successfully secured your Nginx server with Let's Encrypt and enabled automatic certificate renewal.

For more detailed instructions and troubleshooting tips, you can refer to the following resources:

- [DigitalOcean: How to Secure Nginx with Let's Encrypt on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
- [Nginx Blog: Using Free SSL/TLS Certificates from Let's Encrypt with Nginx](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)
- [PhoenixNAP: Let's Encrypt Nginx Tutorial](https://phoenixnap.com/kb/letsencrypt-nginx)

Remember to replace `example.com` and `www.example.com` with your actual domain name.

That's it! You now have a secure Nginx server with HTTPS using Let's Encrypt.

Let me know if you need any further assistance!
