# The FASTEST way to parse email.

```
$ pip install csirtg_mail
$ cat samples/email/single_plain_06.eml| csirtg-mail | jq
[
  {
    "headers": {
      "delivered-to": [
        "phish@csirtgadgets.org"
      ],
      "received": [
        "by 10.112.40.50 with SMTP id u18csp916705lbk;\n        Sun, 19 Apr 2015 05:50:04 -0700 (PDT)",
        "from gmail.com ([61.72.137.254])\n        by mx.google.com with SMTP id s93si13575887ioe.52.2015.04.19.05.50.00\n        for <phish@csirtgadgets.org>;\n        Sun, 19 Apr 2015 05:50:03 -0700 (PDT)"
      ],
      "x-received": [
        "by 10.42.151.4 with SMTP id c4mr13784232icw.77.1429447803846;\n        Sun, 19 Apr 2015 05:50:03 -0700 (PDT)"
      ],
      "return-path": [
        "<advertisebz09ua@gmail.com>"
      ],
      "received-spf": [
        "softfail (google.com: domain of transitioning advertisebz09ua@gmail.com does not designate 61.72.137.254 as permitted sender) client-ip=61.72.137.254;"
      ],
      "authentication-results": [
        "mx.google.com;\n       spf=softfail (google.com: domain of transitioning advertisebz09ua@gmail.com does not designate 61.72.137.254 as permitted sender) smtp.mail=advertisebz09ua@gmail.com;\n       dmarc=fail (p=NONE dis=NONE) header.from=gmail.com"
      ],
      "message-id": [
        "<BE5B7E8D.883B43A2@gmail.com>"
      ],
      "date": [
        "Sun, 19 Apr 2015 05:24:33 -0700"
      ],
      "reply-to": [
        "\"HENRY\" <advertisebz09ua@gmail.com>"
      ],
      "from": [
        "\"HENRY\" <advertisebz09ua@gmail.com>"
      ],
      "user-agent": [
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.19) Gecko/20081209 Thunderbird/2.0.0.19"
      ],
      "mime-version": [
        "1.0"
      ],
      "to": [
        "<phish@csirtgadgets.org>"
      ],
      "subject": [
        "Boost Social Presence with FB posts likes"
      ],
      "content-type": [
        "text/plain;\n    charset=\"us-ascii\""
      ],
      "content-transfer-encoding": [
        "7bit"
      ]
    },
    "mail_parts": [
      {
        "charset": "us-ascii",
        "content_id": null,
        "description": null,
        "disposition": null,
        "filename": null,
        "is_body": "text/plain",
        "sanitized_filename": null,
        "type": "text/plain",
        "decoded_body": "You may not know me and you are probably wondering why you are getting this e mail, right?\n\nI'm a hacker who cracked your email and devices a few months ago.\n\nDo not try to contact me or find me, it is impossible, since I sent you an email from YOUR hacked account.\n\nI setup a malware on the adult vids (porno) web-site and guess what, you visited this site to have fun (you know what I mean).\n\nWhile you were watching videos, your internet browser started out functioning as a RDP (Remote Control) having a keylogger which gave me accessibility to your screen and web cam.\n\nafter that, my software program obtained all of your contacts from your Phone, Messenger and email.\n\nYou entered a passwords on the websites you visited, and I intercepted it.\n\nOf course you can will change it, or already changed it.\n\nBut it doesn't matter, my malware updated it every time.\n\nWhat did I do?\n\nI backuped phone. All photo, video and contacts.\n\nI created a double-screen video. 1st part shows the video you were watching (you've got a good taste haha . . .), and 2nd part shows the recording of your web cam.\n\nexactly what should you do?\n\nWell, in my opinion, $1000 (USD) is a fair price for our little secret. You'll make the payment by Bitcoin (if you do not know this, search \"how to buy bitcoin\" in Google).\n\nMy Bitcoin wallet Address:\n\n1KhDTLk95fZQBd5tUXj4123459bBAji2DB\n\n(It is cAsE sensitive, so copy and paste it)\n\nImportant:\n\nYou have 48 hour in order to make the payment. (I've a unique pixel in this e mail, and at this moment I know that you have read through this email message).\n\nTo track the reading of a message and the actions in it, I use the facebook pixel.\n\nThanks to them. (Everything that is used for the authorities can help us.)\n\nMore you can find out by the link.\n\n\nIf I do not get the BitCoins, I will certainly send out your video recording to all of your contacts including relatives, coworkers, and so on. Having said that, if I receive the payment, I'll destroy the video immidiately. If you need evidence, reply with \"Yes!\" and I will certainly send out your video recording to your 6 contacts. It is a non-negotiable offer, that being said don't waste my personal time and yours by responding to this message.\n\n\n",
        "base64_encoded_payload": null
      }
    ],
    "urls": [],
    "btcs": [
      "1KhDTLk95fZQBd5tUXj4123459bBAji2DB"
    ],
    "body_email_addresses": []
  }
]
(csirtgmail) wes@thrall csirtg-mail-py % cat samples/email/single_plain_01.eml| csirtg-mail | jq
[
  {
    "headers": {
      "delivered-to": [
        "phish@csirtgadgets.org"
      ],
      "received": [
        "by 10.112.40.50 with SMTP id u18csp916705lbk;\n        Sun, 19 Apr 2015 05:50:04 -0700 (PDT)",
        "from gmail.com ([61.72.137.254])\n        by mx.google.com with SMTP id s93si13575887ioe.52.2015.04.19.05.50.00\n        for <phish@csirtgadgets.org>;\n        Sun, 19 Apr 2015 05:50:03 -0700 (PDT)"
      ],
      "x-received": [
        "by 10.42.151.4 with SMTP id c4mr13784232icw.77.1429447803846;\n        Sun, 19 Apr 2015 05:50:03 -0700 (PDT)"
      ],
      "return-path": [
        "<advertisebz09ua@gmail.com>"
      ],
      "received-spf": [
        "softfail (google.com: domain of transitioning advertisebz09ua@gmail.com does not designate 61.72.137.254 as permitted sender) client-ip=61.72.137.254;"
      ],
      "authentication-results": [
        "mx.google.com;\n       spf=softfail (google.com: domain of transitioning advertisebz09ua@gmail.com does not designate 61.72.137.254 as permitted sender) smtp.mail=advertisebz09ua@gmail.com;\n       dmarc=fail (p=NONE dis=NONE) header.from=gmail.com"
      ],
      "message-id": [
        "<BE5B7E8D.883B43A2@gmail.com>"
      ],
      "date": [
        "Sun, 19 Apr 2015 05:24:33 -0700"
      ],
      "reply-to": [
        "\"HENRY\" <advertisebz09ua@gmail.com>"
      ],
      "from": [
        "\"HENRY\" <advertisebz09ua@gmail.com>"
      ],
      "user-agent": [
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.19) Gecko/20081209 Thunderbird/2.0.0.19"
      ],
      "mime-version": [
        "1.0"
      ],
      "to": [
        "<phish@csirtgadgets.org>"
      ],
      "subject": [
        "Boost Social Presence with FB posts likes"
      ],
      "content-type": [
        "text/plain;\n    charset=\"us-ascii\""
      ],
      "content-transfer-encoding": [
        "7bit"
      ]
    },
    "mail_parts": [
      {
        "charset": "us-ascii",
        "content_id": null,
        "description": null,
        "disposition": null,
        "filename": null,
        "is_body": "text/plain",
        "sanitized_filename": null,
        "type": "text/plain",
        "decoded_body": "Hello,\nBoost your Facebook posts with a massive promotion \nand gain over 10.000 likes in total towards all your posts. \n\nWe can promote up to 20 posts links at a time. \n\nIncrease exposure with guaranteed promotion service.\n\nUse this coupon and get another 10% discount on your purchase\n\n==================\n10% Coupon = EB2CA\n==================\n\nOrder today, cheap and guaranteed service:\nhttp://www.socialservices.cn/detail.php?id=9\n\nRegards\nHENRY\nÂ \n\n\n\n\n\n\nUnsubscribe option is available on the footer of our website\n\n\n\n",
        "base64_encoded_payload": null
      }
    ],
    "urls": [
      "http://www.socialservices.cn/detail.php?id=9"
    ],
    "btcs": [],
    "body_email_addresses": []
  }
]

```

# Getting Help

Need more advanced help? [Partner with us!](https://csirtg.io/support)

# COPYRIGHT AND LICENSE

Copyright (C) 2021 [CSIRT Gadgets](http://csirtgadgets.com)

Free use of this software is granted under the terms of the [Mozilla Public License (MPLv2)](https://www.mozilla.org/en-US/MPL/2.0/).
