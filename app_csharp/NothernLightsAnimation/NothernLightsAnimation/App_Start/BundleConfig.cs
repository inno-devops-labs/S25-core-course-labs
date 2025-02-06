using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Optimization;
using System.Web.UI;

namespace NothernLightsAnimation
{
	public class BundleConfig
	{
		// Дополнительные сведения об объединении см. на странице https://go.microsoft.com/fwlink/?LinkID=303951.
		public static void RegisterBundles(BundleCollection bundles)
		{
			RegisterJQueryScriptManager();

			bundles.Add(new ScriptBundle("~/bundles/WebFormsJs").Include(
							"~/Scripts/WebForms/WebForms.js",
							"~/Scripts/WebForms/WebUIValidation.js",
							"~/Scripts/WebForms/MenuStandards.js",
							"~/Scripts/WebForms/Focus.js",
							"~/Scripts/WebForms/GridView.js",
							"~/Scripts/WebForms/DetailsView.js",
							"~/Scripts/WebForms/TreeView.js",
							"~/Scripts/WebForms/WebParts.js"));

			// Для работы этих файлов очень важен порядок, так как у них есть явные зависимости
			bundles.Add(new ScriptBundle("~/bundles/MsAjaxJs").Include(
					"~/Scripts/WebForms/MsAjax/MicrosoftAjax.js",
					"~/Scripts/WebForms/MsAjax/MicrosoftAjaxApplicationServices.js",
					"~/Scripts/WebForms/MsAjax/MicrosoftAjaxTimer.js",
					"~/Scripts/WebForms/MsAjax/MicrosoftAjaxWebForms.js"));

			// Используйте версию Modernizr для разработчиков, чтобы учиться работать. Когда вы будете готовы перейти к работе,
			// готово к выпуску, используйте средство сборки по адресу https://modernizr.com, чтобы выбрать только необходимые тесты.
			bundles.Add(new ScriptBundle("~/bundles/modernizr").Include(
							"~/Scripts/modernizr-*"));
		}

		public static void RegisterJQueryScriptManager()
		{
			ScriptManager.ScriptResourceMapping.AddDefinition("jquery",
				new ScriptResourceDefinition
				{
					Path = "~/scripts/jquery-3.7.0.min.js",
					DebugPath = "~/scripts/jquery-3.7.0.js",
					CdnPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.0.min.js",
					CdnDebugPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.0.js"
				});
		}
	}
}