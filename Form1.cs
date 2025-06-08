using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace PowerShellv2
{
    static class cizgi
    {
        public const string tırnak = " \"";
    }

    public partial class Form1 : Form
    {
        public Form1()
        {
            RunScript("sdfsd", "asv");
            InitializeComponent();

            baslangıcTarihi.Format = DateTimePickerFormat.Custom;
            baslangıcTarihi.CustomFormat = "yyyy-M-d";
            
            bitisTarihi.Format = DateTimePickerFormat.Custom;
            bitisTarihi.CustomFormat = "yyyy-M-d";

        }
     
        private string RunScript(string script , string tarih)
        {
            //scrapy crawl TweetScraper - a query = "darbe until:2016-4-4"
            //scrapy crawl TweetScraper - a query = "Darbe, #DarbeyeHayır until:2018-07-07"
            string strCmdText;
            //For Testing


            //strCmdText = "/k scrapy crawl TweetScraper -a query=" + tirnak + script + " until: " + tarih + tirnak;
            
            //strCmdText = "/k scrapy crawl TweetScraper -a query='asdsasa since: 2020-05-05'" 
           // strCmdText = strCmdText.Replace("\"" , "");
            System.Diagnostics.Process.Start("CMD.exe", strCmdText);
            return null;
        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dtb;
            dtb = baslangıcTarihi.Value;
            DateTime dtf;
            dtf = bitisTarihi.Value;

            textBox1.Text = RunScript(textBox1.Text , textBox2.Text);
        }

    }
}
